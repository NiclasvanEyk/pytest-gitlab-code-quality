# Contributing

## Setup

The project uses [uv](https://github.com/astral-sh/uv), but feel free to install or setup the required packages using plain `pip` or whatever you prefer.

Install the dependencies using

```shell
uv sync
```

and run the tests using

```shell
uv run pytest
```

The project also uses `ruff` as a linter and formatter, so you may use

```shell
uv run ruff check
```

to run automated checks and

```shell
uv run ruff format
```

to automatically format your code.
Both of these steps will run automatically in GitHub actions on every PR.
