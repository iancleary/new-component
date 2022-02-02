# Python template repository

[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://black.readthedocs.io/en/stable/)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![ci](https://github.com/iancleary/template-python/workflows/ci/badge.svg)](https://github.com/iancleary/template-python/actions/workflows/ci.yml)

Ian Cleary ([iancleary](https://github.com/iancleary))

## Description

**Welcome!** This is a template repository for Python projects, engineered for use as a [GitHub template repository](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-from-a-template). To use the template, click on "Use this template" or browse to [template-python/generate](https://github.com/iancleary/template-python/generate). GitHub will create a new repository without the commit history from this one.

The `template-python` repo name can be replaced with a one-line terminal command: `git grep -l 'template-python' | xargs sed -i '' 's/template-python/repo-name/g'` (replace `repo-name` with the name of the repository you generate). There may also be a few edits to the _pyproject.toml_ needed. See the [quickstart](#quickstart) section for more.
## Quickstart

```sh
❯ cd path/to/repo
# Replace instances of template-python with new repo name
# In the command below, use your repo name instead of 'repo-name'
❯ git grep -l 'template-python' | xargs sed -i '' 's|template-python|repo-name|g'
❯ git grep -l 'new_component' | xargs sed -i '' 's|new_component|repo-name|g'
# Install virtual environment with poetry: https://python-poetry.org/docs/
❯ poetry install
❯ poetry shell
# Install pre-commit hooks
.venv ❯ pre-commit install
# Try running the tests
.venv ❯ pytest
```

## Further information

See [CONTRIBUTING.md](.github/CONTRIBUTING.md).
