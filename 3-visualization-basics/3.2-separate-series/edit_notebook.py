import nbformat
from nbformat import v4 as nbf

# Function to create a new notebook with introductory text and example code cells
def create_notebook_with_content():
    nb = nbf.new_notebook()
    nb.cells.append(nbf.new_markdown_cell("""\
# NFL Data Visualization with Pandas

In this tutorial, we will explore how to create various types of charts using the pandas plotting API. We will use NFL data to visualize team performance statistics over time. We'll start with scatter plots, which are a great way to visualize two variables and their relationship to one another. Then, we'll move on to bar charts and line charts, which help us compare different groups and show trends over time, respectively.

## Scatter Plots
Before we dive into the code, let's understand what scatter plots are and why they are useful. Scatter plots allow us to observe the relationship between two continuous variables; for example, we might want to see if there's a correlation between the number of touchdowns and the number of wins for a team.

Here's how you can create a scatter plot using pandas:
"""))
    nb.cells.append(nbf.new_code_cell("""\
import pandas as pd

# Load your data here
data = pd.read_csv('standings.csv')

# Example scatter plot
# Let's plot touchdowns vs. wins
data.plot.scatter(x='touchdowns', y='wins')

# The plot function is very flexible. For instance, you could add a 'hue' parameter to color the points by another category.
"""))
    nb.cells.append(nbf.new_markdown_cell("""\
## Bar Charts
Bar charts are useful for comparing quantities corresponding to different groups. For example, we might want to compare the average number of wins across different divisions.

Here's a simple bar chart using pandas:
"""))
    nb.cells.append(nbf.new_code_cell("""\
# Example bar chart
# Let's compare the average number of wins by division
data.groupby('division')['wins'].mean().plot.bar()

# With pandas, you can easily create stacked bar charts by passing stacked=True, or create horizontal bar charts with kind='barh'.
"""))
    nb.cells.append(nbf.new_markdown_cell("""\
## Line Charts
Line charts are perfect for showing trends over time. For instance, we might be interested in a team's performance over the course of a season.

Below is how you can create a line chart:
"""))
    nb.cells.append(nbf.new_code_cell("""\
# Example line chart
# Plotting the trend of wins over time for a team
data[data['team'] == 'Patriots'].plot.line(x='date', y='wins')

# The plot function also allows for multiple lines in the same chart, which is useful for comparing trends between groups.
"""))
    nb.cells.append(nbf.new_markdown_cell("""\
## Exercises
Now it's your turn to try creating some plots. Below are some exercises to practice what you've learned. Try to use different options and parameters to customize your plots.
"""))
    nb.cells.append(nbf.new_code_cell("# Exercise 1: Create a scatter plot of two variables of your choice"))
    nb.cells.append(nbf.new_code_cell("# Exercise 2: Create a bar chart showing the distribution of a categorical variable"))
    nb.cells.append(nbf.new_code_cell("# Exercise 3: Create a line chart showing the trend of a variable over time"))
    return nb

# Function to save the notebook
def save_notebook(nb, path):
    with open(path, 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)

# Create the notebook with content
notebook_path = '3.2-separate-series.ipynb'
nb = create_notebook_with_content()

# Save the notebook
save_notebook(nb, notebook_path)
