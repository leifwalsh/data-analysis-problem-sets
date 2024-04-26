import nbformat
from nbformat import v4 as nbf

# Function to load the notebook
def load_notebook(path):
    with open(path, 'r', encoding='utf-8') as f:
        return nbformat.read(f, as_version=4)

# Function to save the notebook
def save_notebook(nb, path):
    with open(path, 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)

# Function to replace matplotlib with pandas plotting
def replace_matplotlib_with_pandas(nb):
    for cell in nb.cells:
        if cell.cell_type == 'code':
            cell.source = cell.source.replace('import matplotlib.pyplot as plt', 'import pandas as pd')
            cell.source = cell.source.replace('plt.', 'pd.')
    return nb

# Function to add empty code cells for exercises
def add_empty_code_cells(nb):
    new_cells = []
    for cell in nb.cells:
        new_cells.append(cell)
        if 'Exercise' in cell.source:
            new_cells.append(nbf.new_code_cell(source='# Your code here'))
    nb.cells = new_cells
    return nb

# Load the notebook
notebook_path = '3.1-scatter-bar-and-line-charts.ipynb'
nb = load_notebook(notebook_path)

# Replace matplotlib with pandas plotting
nb = replace_matplotlib_with_pandas(nb)

# Add empty code cells for exercises
nb = add_empty_code_cells(nb)

# Save the notebook
save_notebook(nb, notebook_path)
