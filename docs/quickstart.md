# Quick Start

## A styled workbook

Each `Column` holds a title and its content. Styles are optional: pass a built-in style, or build
your own with `Style`.

```python
import cellmate as xl

columns = [
    xl.Column(
        title="Product",
        content=["Apples", "Bananas", "Cherries"],
        title_style=xl.TITLE1,
    ),
    xl.Column(
        title="Sales",
        content=[100, 200, 150],
        title_style=xl.TITLE1,
        content_style=xl.Style(name="dollars", number_format="$ #,##0.00"),
    ),
    xl.Column(
        title="Growth",
        content=[0.05, 0.10, 0.07],
        title_style=xl.TITLE1,
        content_style=xl.PERCENTAGE,
    ),
]

sheet = xl.Sheet(data=columns, sheet_name="Summary")
xl.Workbook(sheets=[sheet]).save("summary.xlsx")
```

A single sheet can also be saved on its own, without building a `Workbook`:

```python
sheet.save("summary.xlsx")
```

## Custom styles

A `Style` takes plain dictionaries for font, border, fill and alignment. Anything left out keeps
the default (Calibri 11, no border, no fill, left-aligned).

```python
header = xl.Style(
    name="header",
    font={"bold": True, "color": "FFFFFF"},
    fill={"type": "solid", "color": "10793F"},
    alignment={"horizontal": "center"},
    border={"bottom_style": "thick"},
)
```

Every style needs a unique `name`: cellmate registers it as an Excel named style, so it shows up
in Excel's style gallery too.

## One style per row

`content_style` also accepts a list, with one style per row. Its length must match the content,
or cellmate raises `CellmateException`.

```python
xl.Column(
    title="Value",
    content=[0.25, 1200, 0.031],
    content_style=[xl.PERCENTAGE, xl.CURRENCY, xl.PERCENTAGE_POINTS],
)
```

## Several sheets

```python
workbook = xl.Workbook(sheets=[sales_sheet, costs_sheet])
workbook.save("report.xlsx")
```
