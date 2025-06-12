import pandas as pd

# Load the Iris dataset (using a public URL for convenience)
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df = pd.read_csv(url)

# Display the first few rows of the dataset
print("First few rows of the dataset:")
print(df.head())

# Explore the structure of the dataset
print("\nDataset Info:")
print(df.info())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Clean the dataset (handle missing values if any)
# Since Iris is typically clean, we'll check and handle hypothetically
if df.isnull().sum().sum() > 0:
    # Option 1: Fill missing numerical values with mean
    numerical_cols = df.select_dtypes(include=['float64', 'int64']).columns
    df[numerical_cols] = df[numerical_cols].fillna(df[numerical_cols].mean())
    
    # Option 2: Drop rows with missing values (alternative approach)
    # df = df.dropna()
    
    print("\nMissing values after cleaning:")
    print(df.isnull().sum())
else:
    print("\nNo missing values found in the dataset.")