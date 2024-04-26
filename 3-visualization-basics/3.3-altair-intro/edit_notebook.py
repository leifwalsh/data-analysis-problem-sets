import nbformat
from nbformat.v4 import new_notebook, new_markdown_cell, new_code_cell

# Create a new notebook
nb = new_notebook()

# Add a title to the notebook
nb.cells.append(new_markdown_cell("# Visualization with Altair"))

# Add an introductory markdown cell
intro = """
Altair is a declarative statistical visualization library for Python. It is built on top of Vega and Vega-Lite, which are powerful visualization grammars. With Altair, you can create a wide range of statistical visualizations with a simple and intuitive syntax.

## Advantages of Altair

- **Declarative syntax**: Altair allows you to think about the data rather than the code, making it easier to create complex visualizations.
- **Integration with pandas**: Altair works well with the pandas library, allowing for seamless data manipulation and visualization.
- **Interactive visualizations**: Altair supports interactive features like tooltips, zooming, and panning, which can be very useful for exploring datasets.
"""

nb.cells.append(new_markdown_cell(intro))

# Add a code cell to import Altair and pandas
import_code = """
import altair as alt
import pandas as pd
"""

nb.cells.append(new_code_cell(import_code))

# Add a markdown cell to explain the dataset
dataset_explanation = """
## Iris Dataset

The Iris dataset is a classic dataset in the field of machine learning and statistics. It contains measurements for 150 iris flowers from three different species. We will use this dataset to demonstrate how to create scatter, bar, and line charts with Altair.
"""

nb.cells.append(new_markdown_cell(dataset_explanation))

# Add a code cell to load the Iris dataset
load_dataset_code = """
# Load the Iris dataset
iris = pd.read_csv('iris.csv')
iris.head()
"""

nb.cells.append(new_code_cell(load_dataset_code))

# Add markdown cells and code cells for scatter, bar, and line charts examples

# Scatter plot example
scatter_explanation = """
### Scatter Plot

A scatter plot is useful for visualizing the relationship between two numerical variables. Here, we'll create a scatter plot to examine the relationship between sepal length and sepal width for each species.
"""

scatter_code = """
# Create a scatter plot
alt.Chart(iris).mark_point().encode(
    x='sepalLength',
    y='sepalWidth',
    color='species'
)
"""

nb.cells.append(new_markdown_cell(scatter_explanation))
nb.cells.append(new_code_cell(scatter_code))

# Bar chart example
bar_explanation = """
### Bar Chart

A bar chart is useful for comparing quantities across different categories. Here, we'll create a bar chart to compare the average sepal length of each iris species.
"""

bar_code = """
# Create a bar chart
alt.Chart(iris).mark_bar().encode(
    x='species',
    y='average(sepalLength)'
)
"""

nb.cells.append(new_markdown_cell(bar_explanation))
nb.cells.append(new_code_cell(bar_code))

# Line chart example
line_explanation = """
### Line Chart

A line chart is useful for visualizing data over a continuous interval or time span. In this case, we'll simulate time series data by creating a cumulative sum of sepal length and plot it as a line chart.
"""

line_code = """
# Create a line chart
alt.Chart(iris['sepalLength'].cumsum().reset_index()).mark_line().encode(
    x='index:O',
    y='sepalLength:Q'
)
"""

nb.cells.append(new_markdown_cell(line_explanation))
nb.cells.append(new_code_cell(line_code))

# Save the notebook
nbformat.write(nb, '3.3-altair-intro.ipynb')
