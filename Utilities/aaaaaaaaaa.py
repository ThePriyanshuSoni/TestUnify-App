import pytest


@pytest.mark.regression
def test_browser1():
    print("Test")
    assert 5 == 5


@pytest.mark.xfail
def test_browser2():
    print("Test")
    assert 5 == 5


@pytest.mark.sanity
def test_browser3():
    print("Test")
    assert 5 == 5