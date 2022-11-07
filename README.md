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

- [Features](#features)
  - [Get the loans](#get-the-loans)
- [Usage](#usage)
- [Why I am doing this](#why-i-am-doing-this)
- [Changelog](#changelog)
- [Installation](#installation)
- [Development](#development)
  - [Testing](#testing)
  - [Pre-commit](#pre-commit)
  - [Releasing](#releasing)
- [Credits](#credits)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Features

MédiathèqueRoubaix.py is a client for the **libray of Roubaix**, [mediathequederoubaix.fr](http://www.mediathequederoubaix.fr/).  

<p align="center" width="100%">
  <img src="doc/mr_homepage.png" alt="Screenshot mediathequederoubaix.fr"/>
</p>

### Get the loans

1. Display a **list of your loans** and their due date
2. ...for **many card holders** at once (family) (TODO)
3. and check the **next return date** for all you cards (TODO)

## Usage

```shell
$ export USERNAME="X001002003"
$ export PASSWORD="password00"

$ python src/mediathequeroubaix/main.py
Getting loans of user: X001002003
User: Thomas QUESTE
                                           10 LOANS  
┏━━━━━━━┯━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┯━━━━━━━━━━━━┯━━━━━━━━━━━┓
┃   #   │ Title                                                      │  Due date  │ Renewable ┃
┠───────┼────────────────────────────────────────────────────────────┼────────────┼───────────┨
┃  1/10 │ Opération trolls !                                         │ 12/11/2022 │ ✅        ┃
┃  2/10 │ Le secret du Bagueer                                       │ 12/11/2022 │ ✅        ┃
┃  3/10 │ Le grand pouvoir                                           │ 12/11/2022 │ ✅        ┃
┃  4/10 │ Poursuivie !                                               │ 12/11/2022 │ ✅        ┃
┃  5/10 │ À la recherche d'Ulysse                                    │ 12/11/2022 │ ✅        ┃
┃  6/10 │ Monstrueux dinosaure                                       │ 12/11/2022 │ ✅        ┃
┃  7/10 │ La grande aventure                                         │ 12/11/2022 │ ✅        ┃
┃  8/10 │ Le bonheur est un céphalopode visqueux                     │ 12/11/2022 │ ✅        ┃
┃  9/10 │ La folle vie de Bouboule Gum                               │ 12/11/2022 │ ✅        ┃
┃ 10/10 │ Au revoir là-haut                                          │ 19/11/2022 │ ❌        ┃
┗━━━━━━━┷━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┷━━━━━━━━━━━━┷━━━━━━━━━━━┛
```

## Why I am doing this

I created this project to:
1. Learn **Functional Programing**
2. Learn **typed** and **modern** Python
3. Be able to quickly list and renew my loans (especially when you have many cards)

## Changelog

See [CHANGELOG.md](CHANGELOG.md)

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
- Functional library is [Returns from DRY-Python](https://github.com/dry-python/returns)
- Tables look great thanks to [Textualize's Rich](https://github.com/Textualize/rich)
