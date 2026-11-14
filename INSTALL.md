# vininfo installation

[uv](https://docs.astral.sh/uv/) is recommended for installation, though plain `pip` works too.

## From PyPI

Add the package to a project:

```bash
uv add vininfo
```

or with pip:

```bash
pip install vininfo
```

## From source

Clone the repository and synchronize its development environment:

```bash
git clone https://github.com/idlesign/vininfo vininfo
cd vininfo
uv sync
```

Run commands in the project environment with `uv run`.
