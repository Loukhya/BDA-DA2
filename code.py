import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
from minisom import MiniSom
import matplotlib.pyplot as plt

# 1. Load the NSL-KDD Dataset
data = pd.read_csv('NSL-KDD_Dataset.csv')  # Adjust the path if needed

# 2. Preprocess the data
X = data.iloc[:, :-1].values  # Features
y = data.iloc[:, -1].values   # Labels

# Encode categorical variables
label_encoder = LabelEncoder()
for i in range(X.shape[1]):
    if data.dtypes[i] == 'object':
        X[:, i] = label_encoder.fit_transform(X[:, i])

# Normalize the data
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# 3. Initialize the SOM
som = MiniSom(x=20, y=20, input_len=X_scaled.shape[1], sigma=1.0, learning_rate=0.5)

# 4. Train the SOM
som.random_weights_init(X_scaled)
som.train_random(X_scaled, 100)

# 5. Visualize the SOM
plt.figure(figsize=(10, 10))
plt.pcolor(som.distance_map().T, cmap='coolwarm')  # Distance map as background
plt.colorbar()

# Mark data points on the map
for i, x in enumerate(X_scaled):
    w = som.winner(x)  # Winning node
    plt.plot(w[0] + 0.5, w[1] + 0.5, 'o', markerfacecolor='None', markeredgecolor='k', markersize=12, markeredgewidth=2)

plt.title('SOM Cybersecurity Threat Detection')
plt.show()
