
import sys
sys.path.append(r"lecture_05_unit_tests")

from hello import hello

def test_default_hello():
    assert hello() == "Hello, World!"

def test_argument():
    assert hello("Alice") == "Hello, Alice!"
