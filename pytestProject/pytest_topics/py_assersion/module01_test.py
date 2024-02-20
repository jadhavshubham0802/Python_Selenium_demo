def test_a1():
    assert 4 != 1

def test_a2():
    assert 1   #true

def test_a3():
    assert 1 in divmod(4, 2)
    assert "abd" == 'abc'  #comparing string

def test_a4():
    assert "put" in "put it right"   # finding substring in string
    assert "pytest" not in "put it right" #pass
def test_a5():
     assert [1,2] in [1,2,3]  #it will fail
     assert 1 in [1,2,4]  #it will be pass

