# Step 1: Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay


# Step 2: Load the Iris Dataset
iris = load_iris()

# Step 3: Create feature matrix (X) and target vector (y)
X = iris.data
y = iris.target

# Convert to DataFrame for better understanding (optional)
df = pd.DataFrame(X, columns=iris.feature_names)
df['target'] = y

print("Dataset Sample:")
print(df.head())


# Step 4: Split dataset into training and testing sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# Step 5: Create Decision Tree Classifier model
model = DecisionTreeClassifier(random_state=42)


# Step 6: Train the model
model.fit(X_train, y_train)


# Step 7: Predict the class labels for test data
y_pred = model.predict(X_test)


# Step 8: Evaluate the model

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print("\nModel Evaluation")
print("Accuracy:", round(accuracy,4))


# Classification Report
print("\nClassification Report")
print(classification_report(y_test, y_pred, target_names=iris.target_names))


# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix")
print(cm)


# Step 9: Visualize Confusion Matrix
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=iris.target_names)
disp.plot()

plt.title("Confusion Matrix - Decision Tree")
plt.show()