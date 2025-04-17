import pandas as pd
import numpy as np
import ta  # technical analysis indicators
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.utils import to_categorical
from sklearn.metrics import classification_report
import glob


dfFile = file_paths = glob.glob("data/*.csv")

dfList = [pd.read_csv(file, parse_dates=['time']) for file in file_paths]

df = pd.concat(dfList)

#combine Date and time
df['time'] = pd.to_datetime(
    df['date'].astype(str) + ' ' + df['time'].astype(str),
    format='%Y-%m-%d %H:%M:%S'  # Adjust if your format is different
)


#Gits Rid of the date 
df.drop(columns=['date'], inplace=True)

#sots time by time
df = df.sort_values("time")
df.set_index('time', inplace=True)

#adds other statisctics to help it predic better
df = ta.add_all_ta_features(df, open="open", high="high", low="low", close="close", volume="volume", fillna=True)

#How far I want it to see ahead and how much movement in order to trigure something
future_window = 15  # minutes ahead
threshold = 0.0020  # 25 pips threshold (0.25%)

#Get the return value
df['future_return'] = (df['close'].shift(-future_window) - df['close']) / df['close']

#determines if it is a buy, sell, or hold
def get_label(row):
    if row['future_return'] > threshold:
        return 0  # Buy
    elif row['future_return'] < -threshold:
        return 1  # Sell
    else:
        return 2  # Hold
    
df['label'] = df.apply(get_label, axis=1)



#Data prep

#Droping not neccesary data
df.dropna(inplace=True)
features = df.drop(['label', 'future_return'], axis=1)
labels = df['label']

#Normalize feature values using Standard Scaler
scaler = StandardScaler()
X = scaler.fit_transform(features)

#converts languale to catogories
y = to_categorical(labels, num_classes=3)


#80/20 Train/Test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, shuffle=False
)

#train
model = Sequential([
    Dense(128, activation='relu', input_shape=(X_train.shape[1],)),
    Dropout(0.3),
    Dense(64, activation='relu'),
    Dense(3, activation='softmax')  # 3 classes: buy, sell, hold
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

model.fit(X_train, y_train, epochs=10, batch_size=64, validation_split=0.1)


#Test
predictions = model.predict(X_test)
pred_classes = predictions.argmax(axis=1)
true_classes = y_test.argmax(axis=1)

print(classification_report(true_classes, pred_classes, target_names=['Buy', 'Sell', 'Hold']))






