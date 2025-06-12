import pandas as pd

# Load the Iris dataset
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df = pd.read_csv(url)

# Compute basic statistics for numerical columns
print("Basic Statistics for Numerical Columns:")
print(df.describe())

# Group by the categorical column 'species' and compute the mean of numerical columns
print("\nMean of Numerical Columns by Species:")
group_means = df.groupby('species').mean()
print(group_means)

# Optional: To make the output cleaner, round the means to 2 decimal places
print("\nMean of Numerical Columns by Species (Rounded):")
print(group_means.round(2))