# RequestIndetifier class
My implementation of class for programming task in Visma Solutions Summer Trainee recruitment process.

## Installation

Application is written and it is tested with Python 3.8 and it's dependencies are managed with [Poetry](https://python-poetry.org/). 

1. Copy repository from GitHub

2. Install dependencies with command
```bash
poetry install
```

## Usage

Run program with command
```bash
poetry run invoke start
```

Run tests with command
```bash
poetry run invoke test
```

Create coverage report (/htmlcov/index.html) with command
```bash
poetry run invoke coverage-report
```

## Description of design and implementation process

To begin the process, I created framework for the Python application. I decided to use Poetry for dependency management, Pytest for testing and Coverage for test coverage reporting. I also wanted easy to use commands, and for that I added Invoke as a dependency. I also created files for RequestIdentifier and IdentifierClient classes and test file for the former.

After this I started to work on URI parsing using test driven development. Everything went quite smoothly until I started to work on confirm paths, where I needed to validate and apply integer type to parameter paymentnumber. I had luck when I defined values in paths_and_requirements to be the required type of each parameter, so I was able to proceed with very little trial and error.

Last step was to create the client class. I had to spend some time trying to understand the functionality of this required class. I ended up writing a small CLI program, where user can input uri-strings and program returns path and parameter information based on the input. Manual testing with this client revealed some validation bugs, which I wrote tests for and fixed.

There is still some refactoring which could be done. For example method parse_and_validate_uri does a lot of different things and some of those steps could be separated to different methods in the same way as parse_parameters has already been.
