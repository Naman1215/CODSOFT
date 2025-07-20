# Importing required libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from imblearn.over_sampling import SMOTE
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset with updated file path
df = pd.read_csv(r'C:\Users\LENOVO\Desktop\banking system\Frontend\Codsoft\Credit card\creditcard.csv')

# Display basic information
print("Shape of data:", df.shape)
print("Class distribution:\n", df['Class'].value_counts())

# Separate features and target
X = df.drop('Class', axis=1)
y = df['Class']

# Normalize the feature values
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Handle class imbalance using SMOTE
smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X_scaled, y)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.3, random_state=42)

# Logistic Regression Model
lr_model = LogisticRegression()
lr_model.fit(X_train, y_train)
lr_preds = lr_model.predict(X_test)

# Random Forest Model
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
rf_preds = rf_model.predict(X_test)

# Function to plot confusion matrix
def plot_confusion(y_true, y_pred, title):
    cm = confusion_matrix(y_true, y_pred)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.title(f'Confusion Matrix - {title}')
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.show()

# Evaluation reports
print("\n--- Logistic Regression Classification Report ---")
print(classification_report(y_test, lr_preds))

print("\n--- Random Forest Classification Report ---")
print(classification_report(y_test, rf_preds))

# Plot confusion matrices
plot_confusion(y_test, lr_preds, 'Logistic Regression')
plot_confusion(y_test, rf_preds, 'Random Forest')
