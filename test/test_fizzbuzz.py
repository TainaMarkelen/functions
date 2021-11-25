from functions.src import fizzbuzz

def test_numero3 ():
    assert fizzbuzz.numero(3) == "Fizz"
    
def test_numero5 ():
    assert fizzbuzz.numero(5) == "Buzz"
    
def test_numero9 ():
    assert fizzbuzz.numero (9) == "Fizz"
    
def test_numero15 ():
    assert fizzbuzz.numero (15) == "FizzBuzz"
    
def test_numero7 ():
    assert fizzbuzz.numero (7) == 7