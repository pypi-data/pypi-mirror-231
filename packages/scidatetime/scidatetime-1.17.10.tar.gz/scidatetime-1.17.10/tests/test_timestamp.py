from scidatetime import *


def test_fixed_second():
    v = 1695106243
    x = DateTime(v)
    assert x.getTime() == int(v * 1e3)

def test_second():
    assert DateTime(1695106243) == DateTime('2023-09-19 14:50:43')
