from hello import hello

def test_default_hello():
    assert hello() == "Hello, World!"

def test_argument():
    assert hello("Alice") == "Hello, Alice!"
