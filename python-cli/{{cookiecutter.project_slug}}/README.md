# {{cookiecutter.project_name}}

{{cookiecutter.description}}


## ToC

- [Usage](#usage)


## Usage

Install dependencies with `uv`:

    uv sync

Run your CLI:

    uv run {{cookiecutter.project_slug}} hello --name Tester

Run tests:

    uv run pytest
