import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load the training data
data = pd.read_csv('training_data.csv')

# Separate features (X) and target variable (y)
feature_names = ['number']  # Explicitly provide feature names
X = data[feature_names]
y = data['classification']

# Create a decision tree classifier
model = DecisionTreeClassifier()

# Train the model
model.fit(X, y)

# Get user input
user_input = int(input("Enter a number to predict its classification: "))

# Make a prediction
prediction = model.predict([[user_input]])

# Display the result
print(f"The number {user_input} is predicted to be {prediction[0]}.")
