def fatorial (valor):
    if valor < 0:
        return 0
    i = fat = 1
    while i <= valor:
        fat = fat * i
        i = i + 1
    print("O fatorial de {} é {}".format(valor, fat))
    return fat
      
def entradas ():
    parada = False
    while not parada:
        valor = int(input("Informe um número inteiro positivo: "))
        if valor < 0:
            parada = True
        else:
            (fatorial(valor))
if __name__ == '__main__':
    entradas()