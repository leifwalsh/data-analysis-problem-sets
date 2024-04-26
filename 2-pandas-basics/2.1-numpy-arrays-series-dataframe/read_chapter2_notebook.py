import nbformat

# Function to print the notebook content
def print_notebook_cells(notebook_path):
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)
        for cell in nb.cells:
            print(f"{'Markdown' if cell.cell_type == 'markdown' else 'Code'} Cell:")
            print(cell.source)
            print('-' * 40)

# Path to the notebook file
notebook_file = '2.1-numpy-arrays-series-dataframe.ipynb'

# Print the contents of the notebook
print_notebook_cells(notebook_file)
