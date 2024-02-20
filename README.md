# Data Analysis Problem Sets

This repository contains a sequence of problem sets for practicing working with
data in Python, with Jupyter, pandas, SQL, and a selection of visualization
tools. You can browse the syllabus and jump in wherever feels comfortable or
interesting. If you feel stuck in one area, maybe go back to a previous problem
set to practice.

## Setup

There are three ways to set up an environment to work on these problem sets:

### Jupyter Lite

The easiest way to get started is to open the problem sets in Jupyter Lite,
in your browser. Some Python packages won't come preinstalled, but you can do
most of the initial chapters without installing anything.

Open this project here:
[![lite-badge](https://jupyterlite.rtfd.io/en/latest/_static/badge.svg)](https://leifwalsh.github.io/data-analysis-problem-sets/lab/index.html)

Then, open `README.md` to get started. You can click the links to problem sets
from there.

You can also open any of the problem sets directly from GitHub, by clicking
**"Click here to open this notebook in your browser"** at the top of any
notebook.

### Codespaces

If you have a GitHub account, you can open this project in a Codespace. This
works with VS Code or Jupyter, and will give you a full Python environment
on Linux with all the packages you need preinstalled.

### Devcontainers

If you have VS Code and Docker installed on your computer, you can clone this
repository and open it in a devcontainer. This will give you a full local
Python environment on Linux with all the packages you need preinstalled.

## Syllabus

### Chapter 1: Foundations

Working with command line tools, Jupyter notebooks, and Python.

#### Problem Set 1.1: [Command line tools](./1-foundations/1.1-command-line/1.1-command-line.ipynb)

Learn to run commands and understand their output and errors, navigate
directories, move and copy files.

#### Problem Set 1.2: [Jupyter and Python syntax](./1-foundations/1.2-jupyter-and-python-syntax/1.2-jupyter-and-python-syntax.ipynb)

Work with code cells in a notebook, reason about execution order and state in
Python variables, restarting your kernel.

Python statements, variables, if statements, loops, built in data structures.

#### Problem Set 1.3: [Reading and viewing data](./1-foundations/1.3-reading-and-viewing-data/1.3-reading-and-viewing-data.ipynb)

Read something from a file, without Pandas, and explore it a bit.

#### Problem Set 1.4: Advanced Python

**Note:** You may want to skip this and go straight to Chapter 2 if you're new
to programming. You won't need this until around Chapter 5 or 6.

Defining your own functions, modules, and classes.

### Chapter 2: Pandas basics

Learn the essential pandas operations you'll use frequently.

#### Problem Set 2.1: [numpy arrays, Series, Dataframe](./2-pandas-basics/2.1-numpy-arrays-series-dataframe/2.1-numpy-arrays-series-dataframe.ipynb)

Learn about the core data structures in pandas:
- numpy arrays, which pandas builds on
- The 1-dimensional Series
- The 2-dimensional DataFrame

#### Problem Set 2.2: [Reading CSV and JSON data](./2-pandas-basics/2.2-reading-csv-and-json-data/2.2-reading-csv-and-json-data.ipynb)

Learn how to read data from CSV and JSON files using pandas DataFrames.

#### Problem Set 2.3: [Row and Column selection by location](./2-pandas-basics/2.3-row-and-column-selection-by-location/2.3-row-and-column-selection-by-location.ipynb)

Explore how to select specific rows and columns in a DataFrame.

#### Problem Set 2.4: [Selection by Boolean columns](./2-pandas-basics/2.4-selection-by-boolean-columns/2.4-selection-by-boolean-columns.ipynb)

Explore how to select rows in a DataFrame based on a condition, rather than
their position (or label).

#### Problem Set 2.5: [Indexes: loc[] vs iloc[]](./2-pandas-basics/2.5-indexes-loc-vs-iloc/2.5-indexes-loc-vs-iloc.ipynb)

Explore what "indexes" are in Series and DataFrames.

#### Problem Set 2.6: [Indexes and concatenation](./2-pandas-basics/2.6-indexes-and-concatenation/2.6-indexes-and-concatenation.ipynb)

#### Problem Set 2.7: [Merge and join](./2-pandas-basics/2.7-merge-and-join/2.7-merge-and-join.ipynb)

#### Problem Set 2.8: [Accessors: dates, times, and strings](./2-pandas-basics/2.6-accessors-dates-times-and-strings/2.6-accessors-dates-times-and-strings.ipynb)

#### Problem Set 2.9: [Aggregations](./2-pandas-basics/2.8-aggregations/2.8-aggregations.ipynb)

#### Problem Set 2.10: [Pivot Tables and groupby](./2-pandas-basics/2.9-pivot-tables-and-groupby/2.9-pivot-tables-and-groupby.ipynb)

#### Problem Set 2.11: [Immutable style](./2-pandas-basics/2.10-immutable-style/2.10-immutable-style.ipynb)

#### Problem Set 2.12: [NaN and other gotchas](./2-pandas-basics/2.11-nan-and-other-gotchas/2.11-nan-and-other-gotchas.ipynb)

### Chapter 3: Visualization basics

### Chapter 4: Statistics basics

### Chapter 5: Data oriented thinking

### Chapter 6: Dashboarding

### Chapter 7: Advanced pandas

### Chapter 8: Advanced visualization
