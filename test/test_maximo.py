from functions.src import maximo
    
def test_maximox ():
    assert maximo.maximo(23, 4, 8) == 23
    
def test_maximoy ():
    assert maximo.maximo(6, 45, 9) == 45
    
def test_maximoz ():
    assert maximo.maximo(3, 7, 34) == 34
    
def test_max ():
    assert maximo.maximo(4, 4, 82) == 82
    