import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

# Load historical inflow data
data = pd.read_csv("water_inflow.csv")
values = data['inflow'].values.reshape(-1,1)

# Normalize
scaler = MinMaxScaler()
scaled = scaler.fit_transform(values)

# Prepare sequences
def create_sequences(data, seq_length):
    X, y = [], []
    for i in range(len(data)-seq_length):
        X.append(data[i:i+seq_length])
        y.append(data[i+seq_length])
    return np.array(X), np.array(y)

SEQ_LEN = 10
X, y = create_sequences(scaled, SEQ_LEN)

# Build LSTM
model = Sequential()
model.add(LSTM(50, activation='relu', input_shape=(SEQ_LEN,1)))
model.add(Dense(1))
model.compile(optimizer='adam', loss='mse')

# Train
model.fit(X, y, epochs=50, batch_size=16)

# Prediction function
def predict_next_inflow(last_seq):
    scaled_seq = scaler.transform(last_seq.reshape(-1,1))
    scaled_seq = scaled_seq.reshape((1, SEQ_LEN,1))
    pred_scaled = model.predict(scaled_seq)
    return scaler.inverse_transform(pred_scaled)[0][0]
