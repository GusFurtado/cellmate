# About

## License

cellmate is released under the
[MIT License](https://github.com/GusFurtado/cellmate/blob/main/LICENSE).

## Credits

cellmate is a thin layer over [OpenPyXL](https://openpyxl.readthedocs.io/) (MIT), which does
all the actual reading and writing of Excel files.

## Contributing

The project uses [uv](https://docs.astral.sh/uv/).

```bash
git clone https://github.com/GusFurtado/cellmate
cd cellmate
uv sync
uv run pytest
```

Keep OpenPyXL the only dependency, and add a test for any behaviour change. This site is built
with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) and
[mkdocstrings](https://mkdocstrings.github.io/); preview it with
`uv run --group docs mkdocs serve`.
