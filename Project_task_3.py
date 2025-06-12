import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Set style for better aesthetics
plt.style.use('seaborn')

# Load the Iris dataset
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
iris_df = pd.read_csv(url)

# 1. Line Chart: Synthetic time-series data (monthly sales)
np.random.seed(42)  # For reproducibility
months = pd.date_range(start='2024-01-01', end='2024-12-01', freq='M')
sales = np.random.normal(loc=1000, scale=200, size=len(months)).cumsum()  # Cumulative sales
sales_df = pd.DataFrame({'Date': months, 'Sales': sales})

plt.figure(figsize=(10, 6))
plt.plot(sales_df['Date'], sales_df['Sales'], marker='o', color='b', label='Monthly Sales')
plt.title('Monthly Sales Trend in 2024', fontsize=14)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Sales ($)', fontsize=12)
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('line_chart.png')
plt.close()

# 2. Bar Chart: Average petal length per species
species_means = iris_df.groupby('species')['petal_length'].mean().reset_index()

plt.figure(figsize=(8, 6))
sns.barplot(x='species', y='petal_length', data=species_means, palette='viridis')
plt.title('Average Petal Length by Iris Species', fontsize=14)
plt.xlabel('Species', fontsize=12)
plt.ylabel('Average Petal Length (cm)', fontsize=12)
plt.tight_layout()
plt.savefig('bar_chart.png')
plt.close()

# 3. Histogram: Distribution of sepal length
plt.figure(figsize=(8, 6))
sns.histplot(iris_df['sepal_length'], bins=20, kde=True, color='purple')
plt.title('Distribution of Sepal Length', fontsize=14)
plt.xlabel('Sepal Length (cm)', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.tight_layout()
plt.savefig('histogram.png')
plt.close()

# 4. Scatter Plot: Sepal length vs. petal length
plt.figure(figsize=(8, 6))
sns.scatterplot(x='sepal_length', y='petal_length', hue='species', size='species', data=iris_df, palette='deep')
plt.title('Sepal Length vs. Petal Length by Species', fontsize=14)
plt.xlabel('Sepal Length (cm)', fontsize=12)
plt.ylabel('Petal Length (cm)', fontsize=12)
plt.legend(title='Species')
plt.tight_layout()
plt.savefig('scatter_plot.png')
plt.close()

print("Visualizations saved as: line_chart.png, bar_chart.png, histogram.png, scatter_plot.png")