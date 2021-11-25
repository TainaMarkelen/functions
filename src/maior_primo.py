# caso n não seja primo, a função devolve o maior número primo antes dele

def primo (n):
    i = 2
    resto = 1
            
    while i < n and n >= 2:
        resto = n % i
        i += 1
        if resto == 0:
            n = n - 1
            i = 2
    if resto != 0:
        return (n)

            