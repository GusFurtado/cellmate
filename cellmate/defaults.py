from .components import Style


# Default title styles
TITLE1 = Style(
    name="title1",
    font={"bold": True, "size": 12},
    border={"bottom_style": "thin", "right_style": "thin"},
    fill={"type": "solid", "color": "DDDDFF"},
    alignment={"wrap_text": True, "horizontal": "center"},
)
TITLE2 = Style(
    name="title2",
    font={"bold": True, "size": 12, "color": "FFFFFF"},
    fill={"type": "solid", "color": "021689"},
    alignment={"wrap_text": True, "horizontal": "center"},
    border={
        "top_style": "thin",
        "top_color": "FFFFFF",
        "bottom_style": "thick",
        "bottom_color": "000000",
        "left_style": "thin",
        "left_color": "FFFFFF",
        "right_style": "thin",
        "right_color": "FFFFFF",
    },
)

# Default column styles
DEFAULT = Style(name="default")  # Default style with no specific formatting
PERCENTAGE = Style(name="percentage", number_format="0.00%")
PERCENTAGE_POINTS = Style(name="percentage_points", number_format="0.00 pp")
INTEGER = Style(name="integer", number_format="#,##0")
CURRENCY = Style(name="currency", number_format="$ #,##0.00;-$ #,##0.00")
DATE = Style(name="date", number_format="dd/mm/yyyy")
