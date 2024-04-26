import nbformat

# Function to load the notebook
def load_notebook(path):
    with open(path, 'r', encoding='utf-8') as f:
        return nbformat.read(f, as_version=4)

# Function to resolve conflicts within notebook cells
def resolve_conflicts(notebook):
    resolved_cells = []
    for cell in notebook.cells:
        cell_source = cell.source
        if '<<<<<<<' in cell_source or '=======' in cell_source or '>>>>>>>' in cell_source:
            # Split the cell source into parts based on conflict markers
            parts = cell_source.split('=======')
            before_conflict = parts[0].split('<<<<<<<')[0]
            after_conflict = parts[1].split('>>>>>>>')[1]
            # Here you would determine which part to keep. For simplicity, we keep the part after the conflict
            # In a real scenario, you would have more complex logic to merge changes from both sides
            resolved_source = before_conflict + after_conflict
            cell.source = resolved_source
            resolved_cells.append(cell)
        else:
            resolved_cells.append(cell)
    notebook.cells = resolved_cells
    return notebook

# Function to save the notebook
def save_notebook(nb, path):
    with open(path, 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)

# Load the notebook
notebook_path = '3.1-scatter-bar-and-line-charts.ipynb'
nb = load_notebook(notebook_path)

# Resolve conflicts in the notebook cells
nb = resolve_conflicts(nb)

# Save the resolved notebook
save_notebook(nb, notebook_path)
