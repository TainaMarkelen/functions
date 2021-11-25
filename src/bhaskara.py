if __name__ == '__main__':
    
    a = float(input("Informe um número para a: "))
    b = float(input("Informe um número para b: "))
    c = float(input("Informe um número para c: "))
    
    import math
    def raiz ():
        r = math.sqrt(delta) // (2 * a)
        return r
    
    delta = (b ** 2) - 4 * a * c
    if delta < 0:
        print("Não tem raízes reais") 
    elif delta == 0 or delta > 0:
        x_1 = ( -b + (raiz()))
        x_2 = ( -b - (raiz()))
        if delta == 0:
            print("Tem uma raíz real, que é", x_1)
        else:
            print("Tem duas raízes reais, que são", x_1, "e", x_2)
    
    
    