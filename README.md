<h1 align="center">
    <strong>only-relative-import</strong>
</h1>
<p align="center">
    <a href="https://github.com/Kludex/only-relative-import" target="_blank">
        <img src="https://img.shields.io/github/last-commit/Kludex/only-relative-import" alt="Latest Commit">
    </a>
        <img src="https://img.shields.io/github/workflow/status/Kludex/only-relative-import/CI">
        <a href="https://github.com/Kludex/only-relative-import/actions?workflow=CI" target="_blank">
            <img src="https://img.shields.io/badge/Coverage-100%25-success">
        </a>
    <br />
    <a href="https://pypi.org/project/only-relative-import" target="_blank">
        <img src="https://img.shields.io/pypi/v/only-relative-import" alt="Package version">
    </a>
    <img src="https://img.shields.io/pypi/pyversions/only-relative-import">
    <img src="https://img.shields.io/github/license/Kludex/only-relative-import">
</p>

Linter to only allow relative imports! :sweat_smile:

## Installation

```bash
pip install only-relative-import
```

## Usage

You can either run the CLI or use it in the pre-commit.

### CLI

```bash
only-relative-import --package-name <package_name>
```

### Pre-commit

```yaml
- repo:
    rev: v0.1.0
    hooks:
      - id: only-relative-import
        args: [--package-name, <package_name>]
```


## License

This project is licensed under the terms of the MIT license.
