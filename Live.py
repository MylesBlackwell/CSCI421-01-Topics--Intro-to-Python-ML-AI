from keras.models import load_model
import numpy as np
from sklearn.preprocessing import StandardScaler
from datetime import datetime, timedelta
import pytz
import time
import ta
import requests
import MetaTrader5 as mt5
import pandas as pd
from sklearn.preprocessing import StandardScaler


"""
Name     : MYLES BLACKWELL
Type     : Forex Hedged USD
Server   : MetaQuotes-Demo
Login    : 5035648854
Password : Hh!bN5Nz
Investor : E@ErYs6e

"""

# Connect to MetaTrader 5
if not mt5.initialize():
    print("initialize() failed:", mt5.last_error())
    quit()

# Load model and set timezone
model = load_model("ForexModel.keras")
timezone = pytz.timezone('America/New_York')

# Set features
selected_features = [
    'volatility_bbl', 'volatility_kcl', 'low', 'trend_psar_up', 'others_cr',
    'close', 'open', 'momentum_kama', 'volatility_atr', 'volatility_kcw',
    'volatility_dcw', 'volatility_bbw', 'volatility_ui', 'volatility_dcl'
]

# Get latest price from API
def rate():
    symbol = 'EURUSD'
    tick = mt5.symbol_info_tick(symbol)
    
    #url = f"https://api.twelvedata.com/price?symbol={symbol}&apikey={api_key}"
    #response = requests.get(url)
    #data = response.json()
    
    if tick:
        print(f"Tick Time: {datetime.utcfromtimestamp(tick.time)}")
        print(f"Bid: {tick.bid}, Ask: {tick.ask}")
        return tick.ask
    else:
        raise Exception("Failed to fetch exchange rate")

# Wait until next 1-min mark
def seconds_until_next_min():
    now = datetime.now()
    next_time = now.replace(second=0, microsecond=0) + timedelta(minutes=1)
    return (next_time - now).total_seconds()


def wait_until_next_min():
    sleep_duration = seconds_until_next_min()
    print(f"Waiting {int(sleep_duration)} seconds for next 5-minute interval...")
    time.sleep(sleep_duration)

# Final predictions DataFrame
FinalTesdf = pd.DataFrame(columns=[
    'time', 'open', 'high', 'low', 'close', 'volume', 'predictedTime', 'prediction'
])

general = pd.DataFrame(columns=['time', 'open', 'high', 'low', 'close', 'volume'])

now = datetime.now()
from_time = now - timedelta(minutes=30)
rates = mt5.copy_rates_range("EURUSD", mt5.TIMEFRAME_M1, from_time, now)

new_candles = pd.DataFrame(rates)
new_candles['time'] = pd.to_datetime(new_candles['time'], unit='s')

if 'volume' not in new_candles.columns:
        new_candles['volume'] = 0

general = pd.concat([general, new_candles[['time', 'open', 'high', 'low', 'close', 'volume']]], ignore_index=True)

wait_until_next_min()  # Wait for exact 5-min start

print("Starting")
while True:
    c = datetime.now(timezone)
    formatted = c.strftime('%Y.%m.%d %H:%M')

    open = float(rate())    
    high = 0
    low = open
    close = 0
    volume = 0

    now = datetime.now(timezone)
    mintuteTime = now.strftime('%Y.%m.%d %H:%M')

    while True:  # Inner 1-minute loop
        n = datetime.now(timezone)
        current = n.strftime('%Y.%m.%d %H:%M')

        if current == mintuteTime:
            try:
                live = float(rate())
            except Exception as e:
                print("Error fetching live rate:", e)
                continue

            if live > high:
                high = live
            elif live < low:
                low = live
            time.sleep(1)
            continue
        else:
            try:
                close = float(rate())
                break
            except Exception as e:
                print("Error fetching close rate:", e)
                

    new_data = {
        'time': mintuteTime,
        'open': open,
        'high': high,
        'low': low,
        'close': close,
        'volume': volume
    }

    print("Current Time:", new_data['time'])
    print("Open:", new_data['open'])
    print("High:", new_data['high'])
    print("Low:", new_data['low'])
    print("Close:", new_data['close'])
    print("Volume:", new_data['volume'])

    open = close
    high = close
    low = close

    general = pd.concat([general, pd.DataFrame([new_data])], ignore_index=True)


    try:
        general['volume'] = general['volume'].fillna(0).infer_objects(copy=False)
        general = ta.add_all_ta_features(
            general,
            open="open",
            high="high",
            low="low",
            close="close",
            volume="volume"
            )
    except Exception as e:
        print(f"[ERROR] Failed to compute technical indicators: {e}")
        print(f"THE LEGTH WAS:{len(general)}" )
        continue

    # Prepare for prediction
    features = general[selected_features].iloc[-1:]
    scaler = StandardScaler()
    X = scaler.fit_transform(features)
    prediction = model.predict(X)
    predicted_classes = np.argmax(prediction, axis=1)

    # Map prediction
    prediction_label = {0: "Buy", 1: "Sell", 2: "Hold"}.get(predicted_classes[0], "Unknown")
    predicted_time = (now + timedelta(minutes=15)).strftime('%Y.%m.%d %H:%M')

    # Save result
    # Save result
    new_row = {
        'time': new_data['time'],
        'open': new_data['open'].values[0] if isinstance(new_data['open'], pd.Series) else new_data['open'],
        'high': new_data['high'].values[0] if isinstance(new_data['high'], pd.Series) else new_data['high'],
        'low': new_data['low'].values[0] if isinstance(new_data['low'], pd.Series) else new_data['low'],
        'close': new_data['close'].values[0] if isinstance(new_data['close'], pd.Series) else new_data['close'],
        'volume': new_data['volume'].values[0] if isinstance(new_data['volume'], pd.Series) else new_data['volume'],
        'predictedTime': predicted_time,
        'prediction': prediction_label
    }

    FinalTesdf = pd.concat([FinalTesdf, pd.DataFrame([new_row])], ignore_index=True)
    FinalTesdf.to_csv("live_predictions.csv", index=False)

    # Print the prediction
    print(f"Time: {new_data['time']} | Prediction: {prediction_label}")


    print(f"Time: {formatted} | Prediction: {prediction_label}")
            
    
