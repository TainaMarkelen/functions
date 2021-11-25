def computador_escolhe_jogada (n, m):
    p = 1
    multiplos = 0
    
    while p <= m and multiplos == 0:
        if (n - p) % (m + 1) == 0:
            multiplos += p
        else:
            p += 1
    if m > n:
        multiplos = n
        print ("O computador tirou {} peças.".format(multiplos))       
    elif multiplos == 1:
        print ("O computador tirou uma peça.")
    elif multiplos == 0:
        multiplos += m
        print ("O computador tirou {} peças.".format(multiplos))
    else:
        print ("O computador tirou {} peças.".format(multiplos))
        
    return multiplos
    
        
def usuario_escolhe_jogada (n, m):
    valido = False

    if n < m:
        m = n
    while not valido:

        p = int(input("Quantas peças você vai tirar?: "))
        if p <= 0 or p > m:
            print ("Você precisa tirar um número de peças entre 1 e", m)
        else:
            valido = True
    if p == 1:
        print ("Você tirou uma peça.")
    else:
        print ("Você tirou {} peças.".format(p))
    return p


def partida ():
    peçasvalidas = False
    maximo = False
    while not peçasvalidas:
        n = int(input("Quantas peças? "))
        if n <= 1:
            print ("O número de peças deve ser maior que 1")
        else:
            peçasvalidas = True

    while not maximo:
        m = int(input("Limite de peças por jogada? "))
        if m >= n or m <= 0:
            print("O limite deve ser menor que o total de peças e maior que 1")
        else:
            maximo = True


    p = 1
    multiplo = 0
    computador_venceu = 1
    usuario_venceu = 2
    
    while p <= m and multiplo == 0:
        if (n - p) % (m + 1) == 0:
            multiplo += p
        else:
            p += 1


    if multiplo > 0:
        print ("Computador começa!")
        while n != 0: 
            n = n - (computador_escolhe_jogada (n, m))
            if n == 0:
                print ("Fim do jogo! O computador ganhou!")
                return computador_venceu
            else:
                print ("Agora restam {} peças no tabuleiro.".format(n))
                n = n - (usuario_escolhe_jogada (n, m))
                if n == 0:
                    print ("Fim do jogo! Você ganhou!")
                    return usuario_venceu
                else:
                    print ("Agora restam {} peças no tabuleiro.".format(n))

                   
    
    else:
        print ("Você começa!")
        while n != 0:
            n = n - (usuario_escolhe_jogada (n, m))
            if n == 0:
                print ("Fim do jogo! Você ganhou!")
                return usuario_venceu
            else:
                print ("Agora restam {} peças no tabuleiro.".format(n))
                n = n - (computador_escolhe_jogada (n, m))
                if n == 0:
                    print ("Fim do jogo! O computador ganhou!")
                    return computador_venceu
                else:
                    print ("Agora restam {} peças no tabuleiro.".format(n))


def campeonato ():
    computador_placar = 0
    usuario_placar = 0
    rodada = 1
    
    print ("Voce escolheu um campeonato!")
    
    while rodada <= 3:
        print("**** Rodada {} ****".format(rodada))
        if (partida ()) == 1:
            computador_placar += 1
        else:
            usuario_placar +=1
        rodada += 1

    print("**** Final do campeonato! ****")

    print("Placar: Você {} X {} Computador".format(usuario_placar, computador_placar))
    
if __name__ == '__main__':
    print ("Bem-vindo ao jogo do NIM! Escolha:")
    print ("1 - para jogar uma partida isolada ")
    print ("2 - para jogar um campeonato")
    escolha = int(input(""))
    if escolha == 1:
        print("Voce escolheu uma partida isolada!")
        partida()
    else:
        campeonato ()