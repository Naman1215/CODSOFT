import pandas as pd
import numpy as np
import warnings

# Ignore potential warnings for a cleaner output
warnings.filterwarnings('ignore')

# --- Task 1: Import the dataset using pandas ---

# The file path has been corrected to your specified location.
# The 'r' before the string is important; it tells Python to treat backslashes as literal characters.
file_path = r'C:\Users\LENOVO\Desktop\banking system\Frontend\Codsoft\Movie\IMDb Movies India.csv'

try:
    # Added encoding for broader compatibility, which can prevent other types of errors.
    df = pd.read_csv(file_path, encoding='latin1')
    print("✅ Task 1: Dataset imported successfully!")
    print("-" * 40)
except FileNotFoundError:
    print(f"❌ Error: File not found at the specified path: {file_path}")
    print("Please double-check that 'IMDb Movies India.csv' is inside the 'Movie' folder.")
    exit()

# --- Data Cleaning and Preparation ---
# A copy is made to ensure the original data remains unchanged.
df_cleaned = df.copy()
# The 'Year' column is cleaned (e.g., '(2019)' becomes 2019).
df_cleaned['Year'] = pd.to_numeric(df_cleaned['Year'].str.strip('()'), errors='coerce')
# Rows with missing essential data are dropped to ensure accurate analysis.
df_cleaned.dropna(subset=['Name', 'Year', 'Rating', 'Director', 'Genre'], inplace=True)
# The 'Year' column is converted to a whole number.
df_cleaned['Year'] = df_cleaned['Year'].astype(int)


# --- Task 2: Identify the director with the most movies ---
print("✅ Task 2: Director with the most movies")
most_movies_director = df_cleaned['Director'].value_counts().idxmax()
movie_count = df_cleaned['Director'].value_counts().max()
print(f"The director with the most movies is **{most_movies_director}** with **{movie_count}** movies.")
print("-" * 40)


# --- Task 3: Determine the top 5 genres with the highest average ratings ---
print("✅ Task 3: Top 5 genres with the highest average ratings")
genre_df = df_cleaned[['Genre', 'Rating']].copy()
# Handles movies with multiple genres by splitting them.
genre_df['Genre'] = genre_df['Genre'].str.split(', ')
df_exploded_genre = genre_df.explode('Genre')
# Calculates the average rating for each genre.
top_genres = df_exploded_genre.groupby('Genre')['Rating'].mean().nlargest(5)
print("The top 5 genres by average rating are:")
print(top_genres.to_string())
print("-" * 40)


# --- Task 4: For each year, find the movie with the highest rating ---
print("✅ Task 4: Movie with the highest rating for each year (showing last 10 years)")
# Finds the index of the highest-rated movie for each year.
idx = df_cleaned.loc[df_cleaned.groupby('Year')['Rating'].idxmax()]
top_movies_per_year = idx[['Year', 'Name', 'Rating']].sort_values(by='Year', ascending=False)
print(top_movies_per_year.head(10).to_string(index=False))
print("-" * 40)


# --- Task 5: Create a new column 'Rating_Category' ---
print("✅ Task 5: Create a 'Rating_Category' column")
# Defines the rating brackets.
conditions = [
    df_cleaned['Rating'] >= 8.0,
    (df_cleaned['Rating'] >= 6.0) & (df_cleaned['Rating'] < 8.0)
]
# Defines the labels for each bracket.
choices = ['Excellent', 'Good']
# Creates the new column with 'Average' as the default.
df_cleaned['Rating_Category'] = np.select(conditions, choices, default='Average')
print("New 'Rating_Category' column created. Here's a sample:")
print(df_cleaned[['Name', 'Rating', 'Rating_Category']].head().to_string(index=False))
print("-" * 40)