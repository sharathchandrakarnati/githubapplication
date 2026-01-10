from src.mathoperation import add,sub,mul

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