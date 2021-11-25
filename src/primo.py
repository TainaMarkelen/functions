def primo (n):
    i = 2
    resto = 1
    primo = True

    while i < n and primo:  
        resto = n % i
        i += 1
        if resto == 0:
            primo = False
    if primo:   
        print ("{} é um número primo.".format(n))
    else:
        print ("{} não é um número primo.".format(n))
        
        
if __name__ == '__main__':
    fim = False
    while not fim:
        n = int(input("Informe um número inteiro positivo: "))
        if n <= 0:
            fim = True
        else:
            primo (n)