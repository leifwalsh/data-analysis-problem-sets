import nbformat

# Function to create a new code cell
def create_code_cell(code, cell_id):
    return nbformat.v4.new_code_cell(source=code, metadata={"id": cell_id})

# Function to create a new markdown cell
def create_markdown_cell(markdown, cell_id):
    return nbformat.v4.new_markdown_cell(source=markdown, metadata={"id": cell_id})

# Function to save the notebook
def save_notebook(notebook, path):
    with open(path, 'w', encoding='utf-8') as f:
        nbformat.write(notebook, f)

# Create a new notebook object
nb = nbformat.v4.new_notebook()

# Add cells to the notebook
cells = [
    create_markdown_cell(
        '# Advanced Data Visualization with Altair\n\n'
        'In this section, we will explore more advanced visualization techniques using Altair, '
        'focusing on multiple series, stacked, and grouped bar charts.', 'intro-cell'),

    create_markdown_cell(
        '## The NFL `standings.csv` Dataset\n\n'
        'We will use the NFL `standings.csv` dataset to demonstrate these advanced visualization techniques. '
        'This dataset contains the standings of NFL teams over multiple seasons, which is perfect for '
        'our use case.', 'dataset-cell'),

    create_code_cell(
        'import altair as alt\n'
        'import pandas as pd\n\n'
        '# Load the NFL standings dataset\n'
        'standings = pd.read_csv("standings.csv")\n'
        'standings.head()', 'load-data-cell'),

    create_markdown_cell(
        '### Multiple Series Line Charts\n\n'
        'Multiple series line charts are useful for comparing trends over time across different categories.', 'multi-line-cell'),

    create_code_cell(
        '# Create a multiple series line chart\n'
        'alt.Chart(standings).mark_line().encode(\n'
        '    x="Year:O",\n'
        '    y="Wins:Q",\n'
        '    color="Team:N"\n'
        ').interactive()', 'multi-line-code-cell'),

    create_markdown_cell(
        '### Stacked Bar Charts\n\n'
        'Stacked bar charts allow us to compare parts of a whole across different categories.', 'stacked-bar-cell'),

    create_code_cell(
        '# Create a stacked bar chart\n'
        'alt.Chart(standings).mark_bar().encode(\n'
        '    x="Year:O",\n'
        '    y="Wins:Q",\n'
        '    color="Division:N",\n'
        '    order="Division:N"\n'
        ').interactive()', 'stacked-bar-code-cell'),

    create_markdown_cell(
        '### Grouped Bar Charts\n\n'
        'Grouped bar charts are useful for comparing multiple categories side by side.', 'grouped-bar-cell'),

    create_code_cell(
        '# Create a grouped bar chart\n'
        'alt.Chart(standings).mark_bar().encode(\n'
        '    column="Year:O",\n'
        '    x="Team:N",\n'
        '    y="Wins:Q",\n'
        '    color="Division:N"\n'
        ').interactive()', 'grouped-bar-code-cell'),

    create_markdown_cell(
        '## Advantages of Using Altair\n\n'
        'Altair provides a powerful and concise way to create a wide variety of visualizations, '
        'and its integration with pandas makes it an excellent choice for data analysis in Python.', 'advantages-cell'),

    create_markdown_cell(
        '## Exercises\n\n'
        'Try to create the following visualizations on your own using the `standings.csv` dataset:\n\n'
        '1. A line chart showing the average number of wins per division over time.\n'
        '2. A stacked bar chart showing the total number of wins per conference over time.\n'
        '3. A grouped bar chart comparing the wins and losses of each team in a single year.', 'exercises-cell'),

    create_code_cell('', 'exercise-1-cell'),
    create_code_cell('', 'exercise-2-cell'),
    create_code_cell('', 'exercise-3-cell')
]

# Add cells to the notebook
nb['cells'] = cells

# Save the notebook
save_notebook(nb, '3.4-altair-advanced.ipynb')
