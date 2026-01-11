# Simple Machine Learning example using Linear Regression

import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Training data (House Size vs Price)
# Size in square feet
X = np.array([500, 800, 1000, 1200, 1500]).reshape(-1, 1)

# Price in lakhs
y = np.array([15, 25, 30, 36, 45])

# Create and train the model
model = LinearRegression()
model.fit(X, y)

# Predict price for a new house
new_size = np.array([[1100]])
predicted_price = model.predict(new_size)

print("Predicted price for 1100 sq.ft house:", predicted_price[0], "lakhs")

# Plot the result
plt.scatter(X, y)
plt.plot(X, model.predict(X))
plt.xlabel("House Size (sq.ft)")
plt.ylabel("Price (lakhs)")
plt.title("House Price Prediction using Linear Regression")
plt.show()
