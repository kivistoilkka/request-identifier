# RequestIndetifier class
My implementation of class for programming task in Visma Solutions Summer Trainee recruitment process.

## Installation

Application is written and it is tested with Python 3.8 and it's dependencies are managed with (Poetry)[https://python-poetry.org/]. 

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

## Description of design and implementation process

To begin the process, I created framework for the Python application. I decided to use Poetry for dependency management, Pytest for testing and Coverage for test coverage reporting. I also wanted easy to use commands, and for that I added Invoke as a dependency.
