""" End to end test script """

import subprocess

def test_execution():
    """ test app run """
    result = subprocess.run(["python", "main.py"], capture_output=True, text=True)
    
    assert "Target was successfully found with A*!" in result.stdout
