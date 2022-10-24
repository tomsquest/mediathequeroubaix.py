<p align="center" width="100%">
  <img src="doc/banner.png" alt="MediathequeRoubaix.py"/>
</p>

# Python CLI for the library of Roubaix (Médiathèque Roubaix)

[![PyPI](https://img.shields.io/pypi/v/mediathequeroubaix?style=flat-square)](https://pypi.python.org/pypi/mediathequeroubaix/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/mediathequeroubaix?style=flat-square)](https://pypi.python.org/pypi/mediathequeroubaix/)
[![PyPI - License](https://img.shields.io/pypi/l/mediathequeroubaix?style=flat-square)](https://pypi.python.org/pypi/mediathequeroubaix/)

---

**Source Code**: [https://github.com/tomsquest/mediathequeroubaix.py](https://github.com/tomsquest/mediathequeroubaix.py)

**PyPI**: [https://pypi.org/project/mediathequeroubaix/](https://pypi.org/project/mediathequeroubaix/)

---

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
## Table of Contents

- [Installation](#installation)
- [Development](#development)
  - [Testing](#testing)
  - [Pre-commit](#pre-commit)
  - [Releasing](#releasing)
- [Credits](#credits)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Installation

```sh
pip install mediathequeroubaix
```

## Development

* Clone this repository
* Requirements:
  * [Poetry](https://python-poetry.org/)
  * Python 3.10
* Create a virtual environment and install the dependencies

```sh
poetry install
```

* Activate the virtual environment

```sh
poetry shell
```

### Testing

```sh
pytest
```

### Pre-commit

```sh
pre-commit install
```

Or if you want to run all checks for all files:

```sh
pre-commit run --all-files
```

### Releasing

Trigger the [Draft release workflow](https://github.com/tomsquest/mediathequeroubaix.py/actions/workflows/draft_release.yml)
(press _Run workflow_). This will update the changelog & version and create a GitHub release which is in _Draft_ state.

Find the draft release from the
[GitHub releases](https://github.com/tomsquest/mediathequeroubaix.py/releases) and publish it. When
 a release is published, it'll trigger [release](https://github.com/tomsquest/mediathequeroubaix.py/blob/master/.github/workflows/release.yml) workflow which creates PyPI
 release.


## Credits

- Background and color from [PrettySnap](https://prettysnap.app/)
- Python project bootstrapped using [Wolt template](https://github.com/woltapp/wolt-python-package-cookiecutter)
