import nbformat

# Function to add a markdown cell
def add_markdown_cell(nb, source):
    cell = nbformat.v4.new_markdown_cell(source)
    nb.cells.append(cell)

# Function to add a code cell
def add_code_cell(nb, source):
    cell = nbformat.v4.new_code_cell(source)
    nb.cells.append(cell)

# Load the notebook
with open('3.2-separate-series.ipynb', 'r', encoding='utf-8') as f:
    nb = nbformat.read(f, as_version=4)

# Clear the existing cells
nb.cells.clear()

# Add markdown cells with explanations and code cells with examples

# Expanded introduction markdown cell
intro_markdown = """
# Problem Set 3.2: Multiple Series and Stacked Grouped Charts

In this section, we will delve into advanced visualization techniques using NFL team performance data. We'll start by understanding how to plot multiple series, which is crucial when comparing different categories or groups over a period. This technique helps in identifying trends and patterns across groups.

Next, we'll explore stacked and grouped bar charts. Stacked bar charts are excellent for comparing the part-to-whole relationships within categories over time, while grouped bar charts allow us to compare individual categories side by side. These charts are particularly useful in breaking down complex data into more digestible insights.

By the end of this tutorial, you'll have a solid understanding of these visualization techniques and how to implement them using pandas and matplotlib. Let's get started by loading our data and setting up our environment.
"""

add_markdown_cell(nb, intro_markdown)

# Expanded code cell for data loading with inline comments
data_loading_code = """
import pandas as pd

# Load the NFL data from the CSV file
standings = pd.read_csv('standings.csv')
# Display the first few rows to understand the structure of the data
standings.head()
"""

add_code_cell(nb, data_loading_code)

# Expanded markdown cell for plotting multiple series with more detailed explanation
plotting_series_markdown = """
## Plotting Multiple Series

When dealing with time series data or any data that spans across different categories, plotting multiple series on the same chart is invaluable. It allows for direct comparison between categories, making it easier to spot differences and trends. In the context of NFL data, we can compare the performance of various teams across multiple seasons.

Plotting multiple series is a powerful way to visualize complex data. It enables us to see how different groups or categories change over time relative to each other. This can reveal patterns or anomalies that might not be apparent when looking at single series in isolation. For example, we might discover that certain teams consistently perform better or worse than others, or that there are significant shifts in performance from one season to the next.

Pandas and matplotlib provide a seamless experience for creating multi-series plots. Pandas' data manipulation capabilities allow us to easily structure our data for visualization, while matplotlib gives us the tools to create clear and informative plots. We'll see how to use these libraries to filter our dataset, pivot the data for plotting, and then create a line chart that compares the win percentages of selected NFL teams over time.
"""

add_markdown_cell(nb, plotting_series_markdown)

# Expanded code cell for plotting multiple series with inline comments
plotting_series_code = """
import matplotlib.pyplot as plt

# Filter the data to include only the teams we're interested in
teams_to_plot = ['NE', 'NYJ', 'MIA', 'BUF']
filtered_standings = standings[standings.team.isin(teams_to_plot)]

# Pivot the data to have teams as columns and seasons as rows
# This restructures the DataFrame for easier plotting
pivoted_standings = filtered_standings.pivot(index='season', columns='team', values='pct')

# Create a line chart to visualize the data
# We loop through each team to plot their performance over time
plt.figure(figsize=(10, 6))
for team in teams_to_plot:
    plt.plot(pivoted_standings.index, pivoted_standings[team], marker='o', label=team)

# Add title, labels, and legend to make the chart informative
plt.title('NFL Team Win Percentages Over Time')
plt.xlabel('Season')
plt.ylabel('Win Percentage')
plt.legend(title='Team')
plt.grid(True)
# Display the plot
plt.show()
"""

add_code_cell(nb, plotting_series_code)

# Markdown cell for stacked bar charts
stacked_bars_markdown = """
## Stacked Bar Charts

Stacked bar charts are a type of data visualization that allows us to see how different categories contribute to the total in a single bar for each group. This is particularly useful when we want to understand the part-to-whole relationship within each group. For example, in our NFL data, we might be interested in seeing how each team's win percentage contributes to the total for each season.

These charts can help us identify not only the overall trends but also how the composition of the whole changes over time. They can show us if one category is growing at the expense of another, or if all categories are growing in tandem.

Creating stacked bar charts is straightforward with pandas and matplotlib. Pandas helps us to organize our data into a format that can be easily plotted, and matplotlib provides the functionality to stack the data within the bars. We'll demonstrate how to pivot our data and then plot a stacked bar chart to visualize the win percentages of NFL teams by season.
"""

add_markdown_cell(nb, stacked_bars_markdown)

# Code cell for stacked bar charts
stacked_bars_code = """
# Assuming standings DataFrame is already loaded
# Pivot data to have teams as columns and seasons as rows for win percentages
pivoted_standings = filtered_standings.pivot(index='season', columns='team', values='pct')

# Plot stacked bar chart
pivoted_standings.plot(kind='bar', stacked=True, figsize=(10, 6))
plt.title('NFL Team Win Percentages by Season')
plt.xlabel('Season')
plt.ylabel('Win Percentage')
plt.legend(title='Team')
plt.show()
"""

add_code_cell(nb, stacked_bars_code)

# Markdown cell for grouped bar charts
grouped_bars_markdown = """
## Grouped Bar Charts

Grouped bar charts are an effective way to compare multiple categories side by side. Unlike stacked bar charts, which show the cumulative effect of multiple categories, grouped bar charts allow us to see each category individually, making direct comparisons easier. This can be particularly insightful when we want to compare the performance of different teams across the same seasons.

These charts are useful for highlighting differences between categories and can help us to quickly identify which categories are performing better or worse than others. They are also helpful for spotting trends within individual categories across different groups or time periods.

With pandas and matplotlib, creating grouped bar charts is a simple process. We can use pandas to structure our data appropriately and then leverage matplotlib's plotting capabilities to create a bar chart with groups of bars representing our categories. We'll use this approach to compare the win percentages of NFL teams side by side for each season.
"""

add_markdown_cell(nb, grouped_bars_markdown)

# Code cell for grouped bar charts
grouped_bars_code = """
# Assuming standings DataFrame is already loaded
# Pivot data to have teams as columns and seasons as rows for win percentages
pivoted_standings = filtered_standings.pivot(index='season', columns='team', values='pct')

# Plot grouped bar chart
pivoted_standings.plot(kind='bar', figsize=(10, 6))
plt.title('NFL Team Win Percentages by Season')
plt.xlabel('Season')
plt.ylabel('Win Percentage')
plt.legend(title='Team')
plt.show()
"""

add_code_cell(nb, grouped_bars_code)

# Save the revised notebook
with open('3.2-separate-series.ipynb', 'w', encoding='utf-8') as f:
    nbformat.write(nb, f)
