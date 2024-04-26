import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
iris_data_path = 'iris.data'
column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
iris_df = pd.read_csv(iris_data_path, header=None, names=column_names)

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
