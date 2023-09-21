# PyWidgets

This is a custom widget of `PySide6` modules, which makes it convenient to manage and use as submodules during development.

### Usage

- Add as a submodule

```bash
git submodule add "https://github.com/leoli0605/PyWidgets.git" <local path>
```

- Update

```bash
git submodule update --remote
```

### Widgets

| Widget                                                           | Description | Try It                                                           |
| ---------------------------------------------------------------- | ----------- | ---------------------------------------------------------------- |
| [PyFigureCanvas](./widgets/py_figure_canvas/py_figure_canvas.py) | -           | `poetry run python widgets/py_figure_canvas/py_figure_canvas.py` |
| [PyGraphicsView](./widgets/py_graphics_view/py_graphics_view.py) | -           | `poetry run python widgets/py_graphics_view/py_graphics_view.py` |

### Development

Use [Poetry](https://python-poetry.org/) as the package management tool.

#### Setup

- Windows (Install `Poetry` using `PowerShell`)

```bash
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
$Env:Path += ";$HOME\AppData\Roaming\Python\Scripts"; setx PATH "$Env:Path"
```

- MacOS (Install `Poetry` using [Homebrew](https://brew.sh/))

```bash
brew install poetry
```

#### Environment

```bash
poetry config virtualenvs.in-project true
```

#### Install

- Install dependencies

```bash
poetry install
```

- Install a package

```bash
poetry add <package>
```

- Install a package as a development dependency

```bash
poetry add <package> -G dev
```

- Remove a package

```bash
poetry remove <package>
```

### Coding Style

```bash
poetry run black -l 100 .
```

### Appendix

- Update dependencies

```bash
poetry export -f requirements.txt --output requirements.txt --without-hashes
```
