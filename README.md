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

After this I started to work on URI parsing using test driven development. Everything went quite smoothly until I started to work on validation of confirm path, where I needed to validate and apply integer type to parameter paymentnumber. I had luck when I had defined values in paths_and_requirements to be the required type of each parameter, so I was able to proceed with very little trial and error.

Last step was to create the client class. I had to spend some time trying to understand the required functionality of this class. I ended up writing a small CLI program, where user can input uri strings and program returns path and parameter information based on the input or error message in case of invalid uri strings. Manual testing with this client revealed one validation bug, which I wrote test for and fixed.

There is still some refactoring which could be done. I was able to do some refactoring before the 3 hour time limit. But I think there is quite good separation of concerns between methods and this class can be easily expanded to accept new paths by modifying paths_and_requirements dictionary. I am quite happy with the result.
