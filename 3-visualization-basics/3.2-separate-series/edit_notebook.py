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

Welcome to the tutorial on advanced data visualization techniques using the NFL team performance data. In this section, we will cover how to effectively compare and analyze data across different categories or groups over time using multiple series plots. This is a key skill in data analysis that can help uncover trends and patterns that are not immediately obvious.

We will also dive into the intricacies of stacked and grouped bar charts. These types of charts are powerful tools for breaking down and understanding complex datasets. Stacked bar charts allow us to examine part-to-whole relationships within categories, while grouped bar charts enable us to compare these categories side by side.

Throughout this tutorial, we will use pandas for data manipulation and matplotlib for creating our visualizations. By the end of this section, you will be equipped with the knowledge to implement these visualization techniques and apply them to your own data analysis projects. Let's begin by setting up our environment and loading the data we will be working with.
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

# Filter the data to include only the divisions we're interested in
divisions_to_plot = standings['division'].unique()

# Pivot the data to have divisions as columns and seasons as rows
# This restructures the DataFrame for easier plotting
pivoted_standings = standings.pivot_table(index='season', columns='division', values='win_pct', aggfunc='mean')

# Create a line chart to visualize the data
# We loop through each division to plot their performance over time
plt.figure(figsize=(10, 6))
for division in divisions_to_plot:
    plt.plot(pivoted_standings.index, pivoted_standings[division], marker='o', label=division)

# Differentiate conferences by color
conference_colors = {'AFC': 'blue', 'NFC': 'green'}
for conference in standings['conference'].unique():
    conference_divisions = standings[standings['conference'] == conference]['division'].unique()
    for division in conference_divisions:
        plt.plot(pivoted_standings.index, pivoted_standings[division], marker='o', label=f"{conference} - {division}", color=conference_colors[conference])

# Add title, labels, and legend to make the chart informative
plt.title('NFL Division Win Percentages Over Time')
plt.xlabel('Season')
plt.ylabel('Win Percentage')
plt.legend(title='Division')
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

# Markdown cell for grouping by division and conference
grouping_markdown = """
## Grouping by Division and Conference

In addition to comparing team performance, we can analyze how teams perform on a larger scale by grouping them into divisions and conferences. This allows us to see broader trends and make comparisons on a higher level of aggregation.

Let's calculate and plot the mean and quantiles of win percentages grouped by division and conference. This will give us insights into the overall performance characteristics of these groups.

### Mean Win Percentage by Division

First, we'll calculate the mean win percentage for each division and plot a bar chart to visualize it.
"""
add_markdown_cell(nb, grouping_markdown)

# Code cell for mean win percentage by division
mean_division_code = """
# Calculate the mean win percentage by division
mean_win_pct_by_division = standings.groupby('division')['win_pct'].mean()

# Plot the mean win percentage by division
mean_win_pct_by_division.plot(kind='bar', figsize=(10, 6))
plt.title('Mean Win Percentage by Division')
plt.xlabel('Division')
plt.ylabel('Mean Win Percentage')
plt.show()
"""
add_code_cell(nb, mean_division_code)

# Markdown cell for win percentage quantiles by conference
quantiles_conference_markdown = """
### Win Percentage Quantiles by Conference

Next, we'll calculate the quantiles of win percentages for each conference. This will show us the distribution of team performance within each conference.

We'll plot the 25th, 50th (median), and 75th percentiles for each conference.
"""
add_markdown_cell(nb, quantiles_conference_markdown)

# Code cell for win percentage quantiles by conference
quantiles_conference_code = """
# Calculate the quantiles of win percentage by conference
quantiles_by_conference = standings.groupby('conference')['win_pct'].quantile([0.25, 0.5, 0.75]).unstack()

# Plot the quantiles of win percentage by conference
quantiles_by_conference.plot(kind='bar', figsize=(10, 6))
plt.title('Win Percentage Quantiles by Conference')
plt.xlabel('Conference')
plt.ylabel('Win Percentage')
plt.legend(title='Quantile')
plt.show()
"""
add_code_cell(nb, quantiles_conference_code)

# Markdown cell for example problems
example_problems_markdown = """
## Example Problems

Now that you've learned about plotting multiple series, stacked and grouped bar charts, and grouping statistics, it's time to put your knowledge to the test. Below are a few problems for you to solve using the NFL data. Try to work through these on your own before looking at the solutions.

1. **Divisional Dominance**: Using a line chart, plot the mean win percentage for each division over the last five seasons. Which division appears to be the strongest?

2. **Conference Comparison**: Create a stacked bar chart showing the win percentage for each conference, with the bars divided by division. What trends do you notice about the divisions within each conference?

3. **Performance Peaks**: Using a scatter plot, visualize the 75th percentile of win percentages for teams in the 'NFC East' division over time. What does this tell you about the top-performing teams in this division?

Remember to label your axes and provide a legend where necessary to make your charts informative.
"""
add_markdown_cell(nb, example_problems_markdown)

# Save the revised notebook
with open('3.2-separate-series.ipynb', 'w', encoding='utf-8') as f:
    nbformat.write(nb, f)
