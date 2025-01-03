# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 17:51:45 2025

@author: miaol
"""

# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# 1. Load the Iris dataset
iris = load_iris()
# Convert it into a pandas DataFrame
data = pd.DataFrame(iris.data, columns=iris.feature_names)
# Add the target column (species)
data['species'] = iris.target

# Map the target numbers to species names
data['species'] = data['species'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})

# 2. Inspect the dataset
print("First 5 rows of the dataset:")
print(data.head())  # Display the first 5 rows

print("\nDataset Information:")
print(data.info())  # Display dataset information (columns, types, missing values)

print("\nSummary Statistics:")
print(data.describe())  # Display summary statistics

# 3. Exploratory Data Analysis (EDA)
# Example: Visualize the distribution of sepal length
plt.hist(data['sepal length (cm)'], bins=20, color='blue', edgecolor='black')
plt.title('Distribution of Sepal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.show()

# Example: Scatter plot between petal length and petal width
plt.scatter(data['petal length (cm)'], data['petal width (cm)'], alpha=0.7, c=data['species'].map({'setosa': 0, 'versicolor': 1, 'virginica': 2}), cmap='viridis')
plt.title('Petal Length vs Petal Width by Species')
plt.xlabel('Petal Length (cm)')
plt.ylabel('Petal Width (cm)')
plt.colorbar(ticks=[0, 1, 2], label='Species')
plt.show()

# 4. Perform basic data analysis
# Example: Compute the mean petal length by species
mean_petal_length = data.groupby('species')['petal length (cm)'].mean()
print("\nMean Petal Length by Species:")
print(mean_petal_length)

# Example: Correlation between petal length and petal width
correlation = data['petal length (cm)'].corr(data['petal width (cm)'])
print(f"\nCorrelation between Petal Length and Petal Width: {correlation:.2f}")

# 5. Save results
# Save the dataset with species names to a CSV file
data.to_csv('iris_dataset.csv', index=False)
print("\nIris dataset saved to 'iris_dataset.csv'.")
