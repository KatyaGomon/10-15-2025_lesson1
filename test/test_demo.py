import pytest

@pytest.fixture()
def before_after():
    print('Before test')
    yield
    print('\nAfter test')

def test_demo1(before_after):
    assert 1 == 1

def test_demo2():
    assert 2 == 2

def test_demo3():
    assert 2 == 3