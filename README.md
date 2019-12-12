# Sudoku Solver

This is backend application for a step-by-step sudoku solver project

## Development

Download copy of this repo and install requirements:

```bash
pip install -r requirements/requirements.txt -r requirements/dev-requirements.txt
```

Install pre-commit hooks:
```bash
pre-commit install
```

Set env variables (see [dev.env](dev.env)):

```bash
export PYTHONPATH=solvesudoku
export DJANGO_DEBUG=1
export DJANGO_SECRET_KEY=not_a_secret_key
```

Run development server:

```bash
python manage.py runserver
```

To run test:

```bash
pytest
```

## Deployment

To deploy application just push a new tag to the repository
