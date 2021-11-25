from functions.src import vogal

def test_vogala():
    assert vogal.vogal("a") == True
    
def test_vogalb():
    assert vogal.vogal("b") == False
    
def test_vogalA():
    assert vogal.vogal("A") == True