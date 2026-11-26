<p align="center">
  <img class="hero" src="https://www.gustavofurtado.com/assets/img/projects/cellmate.png" alt="cellmate" width="100%">
</p>

**Styled Excel spreadsheets with OpenPyXL, in a few lines of Python.**

OpenPyXL can format every detail of a spreadsheet, one cell at a time. cellmate puts a thin layer
on top of it: describe each column once, with its title, content and styles, and cellmate writes
the sheet. Styles are reusable objects, so the same look carries across columns, sheets and
workbooks.

[![PyPI](https://img.shields.io/pypi/v/cellmate)](https://pypi.org/project/cellmate/)
[![Python versions](https://img.shields.io/pypi/pyversions/cellmate)](https://pypi.org/project/cellmate/)
[![Downloads](https://static.pepy.tech/badge/cellmate/month)](https://pepy.tech/projects/cellmate)
[![License](https://img.shields.io/pypi/l/cellmate)](about.md#license)

## Features

- **Columns, not cells**: each column is a title, its content and its styles, written in one go.
- **Reusable styles**: font, border, fill, alignment and number format in one object, registered
  as an Excel named style, so it also shows up in Excel's style gallery.
- **Built-in styles** for titles, currency, percentages, percentage points, integers and dates.
- **One style per row** when a column mixes formats.
- **Still OpenPyXL**: a cellmate `Workbook` is an OpenPyXL `Workbook`, so everything else in
  OpenPyXL keeps working, and OpenPyXL is the only dependency.

## Example

```python
import cellmate as xl

columns = [
    xl.Column(title="Product", content=["Apples", "Bananas", "Cherries"]),
    xl.Column(title="Revenue", content=[1250, 980, 1430],
              content_style=xl.CURRENCY),
    xl.Column(title="Growth", content=[0.05, -0.02, 0.12],
              content_style=xl.PERCENTAGE),
]
xl.Sheet(data=columns, sheet_name="Sales").save("sales.xlsx")
```

## Where to go next

- [Installation](installation.md): one `pip install`, OpenPyXL is the only dependency
- [Quick Start](quickstart.md): a styled workbook in a dozen lines
- [API Reference](reference/components.md): every class and its parameters
- [About](about.md): license, credits and contributing

## Building blocks

| Class | Description |
|---|---|
| [`Style`](reference/components.md#cellmate.components.Style) | Font, border, fill, alignment and number format, reusable across cells |
| [`Column`](reference/components.md#cellmate.components.Column) | A title and its content, with one style for the title and one (or one per row) for the content |
| [`Sheet`](reference/components.md#cellmate.components.Sheet) | A list of columns that becomes a worksheet, or a single-sheet file with `save` |
| [`Workbook`](reference/components.md#cellmate.components.Workbook) | Several sheets in one file; an OpenPyXL `Workbook`, so everything else in OpenPyXL still works |

Common formats (titles, currency, percentages, dates) ship ready to use as
[built-in styles](reference/styles.md).
