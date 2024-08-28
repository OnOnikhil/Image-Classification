import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import xlrd
import pickle
# Load the dataset
dataset = pd.read_excel('cleaned_data.xlsx')

# Select features and target variable
X = dataset.iloc[:, 1:]  # Assuming features start from the second column onwards
y = dataset.iloc[:, 0]   # Assuming the first column is the target variable


# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0, test_size=0.2)

# Scale the features
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)

# Initialize and train the RandomForestClassifier
classifier = RandomForestClassifier(n_estimators=100, random_state=0)
classifier.fit(X_train, y_train)

pickle.dump(classifier, open("model.pkl", "wb"))
