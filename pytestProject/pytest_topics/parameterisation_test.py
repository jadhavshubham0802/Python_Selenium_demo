import pytest

@pytest.mark.parametrize('input', [1,2,3,4])
def test_01(input):
    assert input < 4


# @pytest.mark.parametrize('input_value', [1, 2, 3, 4])
# def test_param01(input_value):
#     assert input_value < 4
