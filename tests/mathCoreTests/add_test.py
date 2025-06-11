import mathCore
import pytest

def test_add():
    assert mathCore.add(2, 3) == 5
    assert mathCore.add(-1, 1) == 0
    assert mathCore.add(0, 0) == 0
    assert mathCore.add(-5, -5) == -10
