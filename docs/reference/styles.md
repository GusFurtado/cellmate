# Built-in styles

Ready-made `Style` instances, available from the top-level package (`cellmate.TITLE1`) or from
`cellmate.styles`.

## Titles

| Style | Look |
|---|---|
| `TITLE1` | Bold 12 pt on light lavender (`DDDDFF`), centered and wrapped, thin bottom and right borders |
| `TITLE2` | Bold white 12 pt on navy (`021689`), centered and wrapped, thick black bottom border |

## Content

| Style | Number format | Example |
|---|---|---|
| `DEFAULT` | `General` | `1234.5` |
| `INTEGER` | `#,##0` | `1,235` |
| `PERCENTAGE` | `0.00%` | `12.35%` |
| `PERCENTAGE_POINTS` | `0.00 pp` | `1.23 pp` |
| `CURRENCY` | `$ #,##0.00;-$ #,##0.00` | `$ 1,234.50` |
| `DATE` | `dd/mm/yyyy` | `31/01/2025` |
