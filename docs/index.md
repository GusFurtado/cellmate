# cellmate

**Styled Excel spreadsheets with OpenPyXL, in a few lines of Python.**

[![PyPI](https://img.shields.io/pypi/v/cellmate)](https://pypi.org/project/cellmate/)
[![Python versions](https://img.shields.io/pypi/pyversions/cellmate)](https://pypi.org/project/cellmate/)
[![Downloads](https://static.pepy.tech/badge/cellmate/month)](https://pepy.tech/projects/cellmate)
[![License](https://img.shields.io/pypi/l/cellmate)](https://github.com/GusFurtado/cellmate/blob/main/LICENSE)

OpenPyXL can format every detail of a spreadsheet, one cell at a time. cellmate puts a thin layer
on top of it: describe each column once, with its title, content and styles, and cellmate writes
the sheet. Styles are reusable objects, so the same look carries across columns, sheets and
workbooks.

## Where to go next

- [Installation](installation.md): one `pip install`, OpenPyXL is the only dependency
- [Quick Start](quickstart.md): a styled workbook in a dozen lines
- [API Reference](reference/components.md): every class and its parameters

## Building blocks

| Class | Description |
|---|---|
| [`Style`](reference/components.md#cellmate.components.Style) | Font, border, fill, alignment and number format, reusable across cells |
| [`Column`](reference/components.md#cellmate.components.Column) | A title and its content, with one style for the title and one (or one per row) for the content |
| [`Sheet`](reference/components.md#cellmate.components.Sheet) | A list of columns that becomes a worksheet, or a single-sheet file with `save` |
| [`Workbook`](reference/components.md#cellmate.components.Workbook) | Several sheets in one file; an OpenPyXL `Workbook`, so everything else in OpenPyXL still works |

Common formats (titles, currency, percentages, dates) ship ready to use as
[built-in styles](reference/styles.md).
