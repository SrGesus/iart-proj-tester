# iart-proj-tester
Unit tests for artificial intelligence project

## Instalation
Clone the repository and install pytest
```bash
git clone https://github.com/SrGesus/iart-proj-tester
cd iart-proj-tester
pip install -r requirements.txt
```
Configure the variables to match your setup
```python
# Test will abort after timeout seconds
timeout = 10
# Path to tests folder
tests_path = "./tests/"
# Path to python script
python_path = "../IArt-PipesMania/pipe.py"
```

## Running
Use pytests to run the tests, e.g:
```bash
python -m pytest --durations=0
```