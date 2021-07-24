print("______________________________________")
print(">DÊ O SEU PALPITE PARA ACERTAR O JOGO<")
print("______________________________________")
print("++++++++++++++++++++++++++++++++++++++")
print("_________DIGITE UM NUMERO___________")

from random import randint
n = int(randint(1,10))
p = 0
t = 0
while p != n:
    p = int(input("Seu palpite> "))
    t += 1
    if p == n:
        print("PARABÊNS! VOCÊ ACERTOU!")
        print("O SEU PLACAR É %i" % t)
    elif p < n:
        print("TENTE UM VALOR MAIOR")
    else:
        print("TENTE UM VALOR MENOR")
print("************************")
print(">VOCÊ GANHOU UM PRÊMIO!<")
print(">----------------------<")
print("************************")

num = input("Digite 1 , 2 ou 3 Para escolher seu Prêmio: ")


if num == '1':
    
    input("PARABÊNS VOCÊ GANHOU UMA MOTO")
    print("Fim do Jogo").end
       
elif num == '2':
    input ("PARABÊNS VOCÊ GANHOU UM FUSCA")
    print("Fim do Jogo").end

elif num == '3':
    input ("PARABÊNS VOCÊ GANHOU UM CURSO NA INFINITY")
    print("Fim do Jogo").end
