<p align="center">
  <a href="https://www.gustavofurtado.com/cellmate/"><img src="https://www.gustavofurtado.com/assets/img/projects/cellmate.png" alt="cellmate" width="640"></a>
</p>

<p align="center">
  <b>Styled Excel spreadsheets with OpenPyXL, in a few lines of Python.</b>
</p>

<p align="center">
  <a href="https://pypi.org/project/cellmate/"><img src="https://img.shields.io/pypi/v/cellmate" alt="PyPI"></a>
  <a href="https://pypi.org/project/cellmate/"><img src="https://img.shields.io/pypi/pyversions/cellmate" alt="Python versions"></a>
  <a href="https://pepy.tech/projects/cellmate"><img src="https://static.pepy.tech/badge/cellmate/month" alt="Downloads"></a>
  <a href="https://github.com/GusFurtado/cellmate/blob/main/LICENSE"><img src="https://img.shields.io/pypi/l/cellmate" alt="License"></a>
</p>

<p align="center">
  <b><a href="https://www.gustavofurtado.com/cellmate/">Documentation</a></b>
</p>

Describe each column once, with its title, content and styles, and cellmate writes the sheet.
Styles are reusable objects, so the same look carries across columns, sheets and workbooks.

## Installation

```sh
pip install cellmate
```

## What's inside

- **`Style`**: font, border, fill, alignment and number format in one reusable object.
- **`Column`**: a title and its content, with a style for each (or one per row).
- **`Sheet`**: a list of columns that becomes a worksheet, or a file of its own.
- **`Workbook`**: several sheets in one file, still a regular OpenPyXL `Workbook`.
- **Built-in styles**: `TITLE1`, `TITLE2`, `CURRENCY`, `PERCENTAGE`, `DATE` and more.

See the [quick start](https://www.gustavofurtado.com/cellmate/quickstart/) and the
[API reference](https://www.gustavofurtado.com/cellmate/reference/components/).
