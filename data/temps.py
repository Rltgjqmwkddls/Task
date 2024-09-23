import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import matplotlib.pyplot as plt

df = pd.read_csv("data/temps.csv", encoding="ms949")
df

df["기온(°C)"].isnull().mean()

df.dropna(inplace=True)

x_data = df[['기온(°C)']]
y_data = df[['지면온도(°C)']]

x_data = torch.FloatTensor(x_data.values)
y_data = torch.FloatTensor(y_data.values)
print(x_data.shape, y_data.shape)

model = nn.Linear(1, 1)
print(model)

plt.figure(figsize=(8, 6))
plt.scatter(x_data, y_data)

model = nn.Linear(1,1)

optimizer = torch.optim.SGD(model.parameters(), lr=0.001)
print(list(model.parameters()))

epochs = 10000

for i in range(epochs + 1):
  y_pred = model(x_data)
  loss = nn.MSELoss()(y_pred, y_data)
  optimizer.zero_grad()
  loss.backward()
  optimizer.step()

  if i % 100 == 0:
    print(f"Epoch: {epochs}/{epochs} Loss: {loss:.6f}")

y_pred = model(x_data).detach().numpy()
y_pred

plt.figure(figsize=(8, 6))
plt.scatter(x_data, y_data)
plt.scatter(x_data, y_pred)

result = model(torch.FloatTensor([[26]]))
result