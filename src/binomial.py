if __name__ == '__main__':

    n = 0
    calc = 0
    divisao = 0
    x = int(input("Informe um número para x: "))
    y = int(input("Informe um número para y: "))
    
    def fatorial (n):
        mult = 1
        while n > 1:
            mult = mult * n
            n = n - 1
        return mult
        
    if x > y:
        calc = (fatorial(y)) * (fatorial(x -y))
        divisao = (fatorial(x)) / calc
        print(divisao)
        
    elif x == y or y == 0:
        print(1)
    elif y == 1:
        print(x)