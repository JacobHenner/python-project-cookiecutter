# python-project-cookiecutter

## Description

*python-project-cookiecutter* is a
[cookiecutter](https://github.com/cookiecutter/cookiecutter) for creating
[typed](https://www.python.org/dev/peps/pep-0484/) Python projects which use
[poetry](https://python-poetry.org/) for dependency management and packaging.

In addition, a set of commonly-used development tools is pre-installed:

* `black`
* `isort`
* `mypy`
* `pytest`
* `coverage`
* `flake8`
* `pylint`
* `bandit`
* `pre-commit`

When a project is created using this cookiecutter, the cookiecutter will
automatically install the included development tools, initialize an empty git
repo, and configure [pre-commit](https://pre-commit.com/) for the newly-created
project.

### Dependencies

To use this cookiecutter, you must have `cookiecutter` and `poetry` installed.

## Usage

`cookiecutter https://github.com/jacobhenner/python-project-cookiecutter`

... or ...

`cookiecutter https://gitlab.com/jacobhenner/python-project-cookiecutter`
