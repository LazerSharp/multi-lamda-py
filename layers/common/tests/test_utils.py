from commonlib import utils

def test_hello_returns_expected_string():
    result = utils.hello("Alice")
    assert "Hello :), Alice" in result
