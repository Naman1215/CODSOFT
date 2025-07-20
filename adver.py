import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# --- 1. Data Exploration and Feature Selection ---

# Updated file path to your specified location.
# The 'r' before the string handles the backslashes correctly in Windows.
file_path = r'C:\Users\LENOVO\Desktop\banking system\Frontend\Codsoft\Adver\advertising.csv'

# Load the dataset
try:
    df = pd.read_csv(file_path)
    print("✅ Dataset imported successfully!")
except FileNotFoundError:
    print(f"❌ Error: File not found at the specified path: {file_path}")
    print("Please double-check that 'advertising.csv' is inside the 'Adver' folder.")
    exit()

# Calculate the correlation between each channel and Sales
print("\n📊 Correlation between Advertising Channels and Sales:")
print(df.corr()['Sales'].sort_values(ascending=False))
print("\n'TV' has the highest correlation (0.901). We will use it as our predictor.")
print("-" * 50)


# --- 2. Model Training ---

# Define the feature (X) and target (y)
# X must be a DataFrame, so we use double brackets [['TV']]
X = df[['TV']]
y = df['Sales']

# Split data into training (80%) and testing (20%) sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)


# --- 3. Model Evaluation and Visualization ---

# Print the model's learned coefficients
intercept = model.intercept_
coefficient = model.coef_[0]

print("🧠 Model Coefficients:")
print(f"Intercept (β₀): {intercept:.4f}")
print(f"TV Coefficient (β₁): {coefficient:.4f}")
print(f"\nRegression Equation: Sales = {intercept:.4f} + {coefficient:.4f} * TV_Budget")
print("-" * 50)

# Visualize the model's fit on the test data
print("📈 Plotting the regression line against actual sales data...")
plt.figure(figsize=(10, 6))
# Scatter plot for the actual data points
sns.scatterplot(x=X_test['TV'], y=y_test, color='blue', label='Actual Sales')
# Plot the regression line from our model's predictions
plt.plot(X_test, model.predict(X_test), color='red', linewidth=2, label='Predicted Sales (Regression Line)')

plt.title('TV Advertising Budget vs. Sales', fontsize=16)
plt.xlabel('TV Advertising Budget ($ Thousands)', fontsize=12)
plt.ylabel('Sales (Thousands of Units)', fontsize=12)
plt.legend()
plt.grid(True)
plt.show()