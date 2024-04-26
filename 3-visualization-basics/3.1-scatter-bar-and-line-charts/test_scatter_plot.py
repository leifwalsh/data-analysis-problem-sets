import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
iris_data_path = 'iris.data'
column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
iris_df = pd.read_csv(iris_data_path, header=None, names=column_names)

# Create a scatter plot
plt.figure(figsize=(8, 6))
for species, group in iris_df.groupby('species'):
    plt.scatter(group['sepal_length'], group['sepal_width'], label=species)
plt.title('Sepal Length vs Sepal Width by Species')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.legend()
plt.show()
