import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
iris_data_path = 'iris.data'
column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
iris_df = pd.read_csv(iris_data_path, header=None, names=column_names)

# Calculate the average sepal length for each species
average_sepal_length = iris_df.groupby('species')['sepal_length'].mean()

# Create a bar chart
average_sepal_length.plot(kind='bar', figsize=(8, 6))
plt.title('Average Sepal Length by Species')
plt.xlabel('Species')
plt.ylabel('Average Sepal Length (cm)')
plt.show()
