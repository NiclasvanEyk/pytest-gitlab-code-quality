# Contributing

## Setup

The project uses [Rye](https://rye-up.com), but feel free to install or setup the required packages using plain `pip` or whatever you prefer.

Install the dependencies using 

```shell
rye sync
```

and run the tests using

```shell
pytest
```

The project also uses `ruff` as a linter and formatter, so you may use

```shell
ruff check
```

to run automated checks and

```shell
ruff format
```

to automatically format your code.
Both of these steps will run automatically in GitHub actions on every PR.

