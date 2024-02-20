import pytest

def test_a1():
    with pytest.raises(Exception):
        assert (1/0)

def fun():
    raise ValueError("Index")

def test_a2():
    with pytest.raises(Exception) as exe:
        fun()
    print(str(exe))
    assert "Index" in (str(exe.value))

