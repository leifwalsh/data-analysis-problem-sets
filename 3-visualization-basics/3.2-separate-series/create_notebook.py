import nbformat
nb = nbformat.v4.new_notebook()
with open('3.2-separate-series.ipynb', 'w', encoding='utf-8') as f:
    nbformat.write(nb, f)
