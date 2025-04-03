import pytest

import cellmate as xl
from cellmate import styles
from cellmate.errors import CellmateException


def test_multisheet_workbook():
    columns1 = [
        xl.Column(["A", "B"], title="str", title_style=styles.TITLE1),
        xl.Column([1, 2], title="int", title_style=styles.TITLE2)
    ]
    sheet1 = xl.Sheet(columns1, sheet_name="multisheet1")

    columns2 = [
        xl.Column([0.5, 1.5], title="currency", content_style=styles.CURRENCY),
        xl.Column([0.5, 1.5], title="percentage", content_style=styles.PERCENTAGE)
    ]
    sheet2 = xl.Sheet(columns2, sheet_name="multisheet2")

    wb = xl.Workbook([sheet1, sheet2])
    wb.save("test_multisheet_workbook.xlsx")


def test_singlesheet_workbook():
    columns = [
        xl.Column([46000, 47000], title="date", content_style=styles.DATE),
        xl.Column([0.5, 1.5], title="int", content_style=[styles.INTEGER, styles.INTEGER]),
    ]
    sheet = xl.Sheet(columns, sheet_name="singlesheet")
    sheet.save("test_singlesheet_workbook.xlsx")


def test_error():
    with pytest.raises(CellmateException) as err:
        xl.Column(
            content=[1, 2, 3],
            title="default",
            content_style=[styles.DEFAULT, styles.PERCENTAGE]
        )
    assert str(err.value) == "Content style length does not match content length"