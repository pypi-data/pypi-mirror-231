# Pydantic Marshals
Library for creating partial pydantic models (automatic converters) from different mappings. Currently, it consists of basic boilerplate parts and functional implementation for sqlalchemy 2.0+ (included via extra)

## Base Interface
TBA

## Implementations
TBA

### SQLAlchemy: Basic usage
TBA

### Assert Contains
The "assert contains" is an interface for validating data, mainly used in testing. Use `"assert-contains"` extra to install this module:
```sh
pip install pydantic-marshals[assert-contains]
```

#### Documentation:
- [Usage with Examples](https://github.com/niqzart/pydantic-marshals/blob/master/docs/assert-contains.md)

## Local development
1. Clone the repository
2. Setup python (the library is made with python 3.11)
3. Install poetry (should work with v1.5.1)
4. Install dependencies
5. Install pre-commit hooks

Commands to use:
```sh
pip install poetry==1.5.1
poetry install
pre-commit install
```
