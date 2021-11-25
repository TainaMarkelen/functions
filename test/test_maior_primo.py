from functions.src import maior_primo

def test_primo2 ():
    assert maior_primo.primo(2) == 2
    
def test_primo3 ():
    assert maior_primo.primo(3) == 3
    
def test_primo4():
    assert maior_primo.primo(4) == 3
    
def test_primo5():
    assert maior_primo.primo(5) == 5
    
def test_primo9():
    assert maior_primo.primo(9) == 7
    
    