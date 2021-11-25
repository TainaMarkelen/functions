from functions.src import maior
   
def test_maiora ():
    assert maior.maior(7, 2) == 7
    
def test_maiorb ():
    assert maior.maior(2, 5) == 5
    
def test_maiorigual ():
    assert maior.maior(4, 4) == "a é igual a b"