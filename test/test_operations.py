from src.mathoperation import add,sub,mul,division

def test_add():
    assert add(2,3)==5
    assert add(5,2)==7

def test_sub():
    assert sub(5,3)==2
    assert sub(8,3)==5
    assert sub(3,3) ==0
def test_mul():
    assert mul(2,1)==2
    assert mul(3,1) == 3
def test_div():
    assert division(3,3)==1
def test_square():
    assert square(2,1) == 1