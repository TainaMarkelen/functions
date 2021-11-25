def eh_primo (x):
    i = 2
    resto = 1
    primo = True
    
    while i < x and primo:  
        resto = x % i
        i += 1
        if resto == 0:
            primo = False       
    return (primo)
    
if __name__ == '__main__':
        limite = int(input("Informe o limite máximo: "))
        
        n = 2
        while n < limite:
            if eh_primo (n):
                print (n, end= ", ")
            n += 1
            
            
            