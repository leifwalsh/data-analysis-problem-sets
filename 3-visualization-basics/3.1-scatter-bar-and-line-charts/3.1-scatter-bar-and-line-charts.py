import pandas as pd
import matplotlib.pyplot as plt

# Introduction
"""
Welcome to Section 3.1 of the Data Analysis Problem Sets. In this section, we will explore how to create scatter, bar, and line charts using the pandas plotting API along with matplotlib. These types of charts are fundamental for data analysis and can help us understand the relationships between different variables in a dataset.

For this tutorial, we will be using the Iris dataset, which is a classic dataset in the field of machine learning and statistics. It contains measurements for 150 iris flowers from three different species.

Let's start by loading the dataset into a pandas DataFrame and taking a quick look at its structure.
"""

# Load the dataset
iris_data_path = 'iris.data'
column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
iris_df = pd.read_csv(iris_data_path, header=None, names=column_names)

# Display the first few rows of the dataframe
print(iris_df.head())

# Scatter Plot Example
"""
Scatter plots are great for visualizing the relationship between two numerical variables. Let's create a scatter plot to compare the sepal length and width of the iris flowers.
"""

# Create a scatter plot
plt.figure(figsize=(8, 6))
for species, group in iris_df.groupby('species'):
    plt.scatter(group['sepal_length'], group['sepal_width'], label=species)
plt.title('Sepal Length vs Sepal Width by Species')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.legend()
plt.show()

# Bar Chart Example
"""
Bar charts are useful for comparing quantities across different categories. We will use a bar chart to compare the average sepal length of each iris species.
"""

# Calculate the average sepal length for each species
average_sepal_length = iris_df.groupby('species')['sepal_length'].mean()

# Create a bar chart
average_sepal_length.plot(kind='bar', figsize=(8, 6))
plt.title('Average Sepal Length by Species')
plt.xlabel('Species')
plt.ylabel('Average Sepal Length (cm)')
plt.show()

# Line Chart Example
"""
Line charts are ideal for showing trends over a sequence. Although the Iris dataset is not a time series, we can still use a line chart to show the variation of petal length across the dataset.
"""

# Sort the dataframe by petal length
sorted_iris_df = iris_df.sort_values('petal_length')

# Create a line chart
plt.figure(figsize=(10, 8))
for species, group in sorted_iris_df.groupby('species'):
    plt.plot(group['petal_length'], label=species)
plt.title('Petal Length Variation by Species')
plt.xlabel('Samples')
plt.ylabel('Petal Length (cm)')
plt.legend()
plt.show()

# Conclusion
"""
In this tutorial, we have seen how to create scatter, bar, and line charts using pandas and matplotlib. These visualizations can help us understand our data better and uncover insights that may not be immediately apparent from the raw numbers.

We encourage you to experiment with different types of charts and datasets to continue honing your data analysis skills.
"""
