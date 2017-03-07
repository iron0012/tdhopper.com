Title: Printing Pandas Data Frames as HTML in Jupyter Notebooks
Date: 2016-03-23
Category: til
Tags: python

Jupyter notebooks nicely render Pandas data frames if they're the last line in a cell. It renders the HTML version of the data frame returned by `pandas.DataFrame.to_html()`. However, if you call `print(df)` in a cell, the data frame is rendered in less readable text-based output.

Despite using Notebooks regularly for years, I'd never bothered to figure out a way around this. However, the solution is easy.

Instead of `print(df)` you use

```python
from IPython.display import display

display(df)
```