def test_imports():
    import requests
    import urllib3
    assert hasattr(requests, "get")
