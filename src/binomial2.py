if __name__ == '__main__':

    n = 0
    calc = 0
    divisao = 0
    pronto = False
    
    def fatorial (n):
        mult = 1
        while n > 1:
            mult = mult * n
            n = n - 1
        return mult
        
    while not pronto:
        x = int(input("Informe um número natural para x: "))
        y = int(input("Informe um número natural para y: "))
        if x < 0 or y < 0:
            print("Os números devem ser positivos")
        elif x < y:
            print("x deve ser maior que y")
        else:
            calc = (fatorial(y)) * (fatorial(x - y))
            divisao = (fatorial(x)) // calc
            print(divisao)
            pronto = True