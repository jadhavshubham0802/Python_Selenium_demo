import pytest
import sys

pytestmark = pytest.mark.skipif(sys.platform == 'win32', reason="will run only on linux")
const= 9/5

def cent_to_fah(cent=0):
    fah = (cent * const) + 32
    return fah

#print(cent_to_fah())

@pytest.mark.skip(reason ="Skipping for no reson")
def test_case01():
    assert type(const) == float

@pytest.mark.skipif(sys.version_info <(3,8), reason="does not work version above")
def test_case02():
    assert cent_to_fah() == 32


@pytest.mark.skipif(cent_to_fah()==32, reason="skipped using function ")
def test_case03():
    assert cent_to_fah() == 32


