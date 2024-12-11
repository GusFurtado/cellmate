# Cellmate

`cellmate` is a Python package for creating and managing styled Excel spreadsheets using OpenPyXL. It provides high-level abstractions such as `Style`, `Column`, `Sheet`, and `Workbook` to simplify Excel operations while allowing for extensive customization and formatting.

## Features
- **Reusable Styles**: Define and apply consistent styles across cells, columns, and sheets.
- **Column Management**: Create structured and styled columns with titles and content.
- **Sheet Creation**: Build sheets with multiple columns, complete with styles and formatting.
- **Workbook Handling**: Manage multiple sheets within a single workbook and save them to Excel files.
- **Built-in Defaults**: Use predefined styles for common formats such as currency, percentage, and dates.

---

## Getting Started

### Prerequisites
Ensure you have Python 3.8 or later installed on your system. Additionally, install the required dependencies:

```bash
pip install openpyxl
```

### Installation
You can install `cellmate` via pip:

```bash
pip install cellmate
```

### Example Usage
Here's an example of how to create a styled Excel workbook using `Cellmate`:

```python
import cellmate as xl

# Define columns with data and styles
columns = [
    xl.Column(
        title="Product",
        content=["Apples", "Bananas", "Cherries"],
        title_style=xl.TITLE1,
        content_style=xl.DEFAULT
    ),
    xl.Column(
        title="Sales",
        content=["100", "200", "150"],
        title_style=xl.TITLE1,
        content_style=xl.Style(name="currency", number_format="$ #,##0.00")
    ),
    xl.Column(
        title="Growth",
        content=["0.05", "0.10", "0.07"],
        title_style=xl.TITLE1,
        content_style=xl.PERCENTAGE
    )
]

# Create a sheet and a workbook
sheet = xl.Sheet(data=columns, sheet_name="Summary")
workbook = xl.Workbook(sheets=[sheet])

# Save the workbook
workbook.save("example.xlsx")
```

---

## Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request on GitHub.

## License
This project is licensed under the MIT License.
