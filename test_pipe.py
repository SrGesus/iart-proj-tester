from subprocess import check_output, TimeoutExpired
import os
import pytest

## Configuration
# Test will abort after timeout seconds
timeout = 10
# Path to tests folder
tests_path = "./tests/"
# Path to python script
python_path = "../IArt-PipesMania/pipe.py"

## Imports python script as module named pipe
## Can be used for more precise unit tests
# import importlib.util
# import sys
# module_name = os.path.basename(python_path)[:-3]
# spec = importlib.util.spec_from_file_location(module_name, python_path)
# pipe = importlib.util.module_from_spec(spec)
# sys.modules["module.name"] = pipe
# spec.loader.exec_module(pipe)

@pytest.mark.parametrize('file_name', [tests_path + "/" + s for s in os.listdir(tests_path) if s.endswith(".txt")])
def test_outputs(file_name):
  file = open(file_name)
  file_out = open(file_name.replace(".txt", ".out"))
  timed_out = False
  try:
    p = check_output(['python3', python_path], stdin=file, timeout=timeout)
    assert str(file_out.read()) == p.decode() # Test
  except TimeoutExpired:
    timed_out = True
  # Had to put in a
  if (timed_out):
    pytest.fail(f'Timed limit exceeded after {timeout} seconds', pytrace=False)


  