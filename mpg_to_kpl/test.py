"""
    MPG to KPL tests.

"""

from converter import convert

def test1():
    assert convert(1) == 0.425

def test2():
    assert convert(32) == 13.605

def test3():
    assert convert(16) == 6.802

def test4():
    assert convert(17.3) == 7.355

def test5():
    assert convert(23.2) == 9.863