import random

numero_aleatorio = random.randrange(1, 100)
valor1 = 10
valor2 = 7
valor3 = 5
dificuldade1 = 1
dificuldade2 = 2
dificuldade3 = 3
print("Jogo de adivinhação")
print("1) Fácil: 10 tentativas")
print("2) Médio: 7 tentativas")
print("3) Difícil: 5 tentativas")

escolha = int(input("Escolha uma dificuldade pelo número: "))
if escolha == 1:
    print("Você tem dez tentativas")
    while valor1 > 0:
        resposta_usuario = int(input("Digite um número: "))
        if resposta_usuario == numero_aleatorio:
            print("Você acertou")
            break
        else:
            print("Você errou")
            if resposta_usuario > numero_aleatorio:
                print("O número está abaixo de", resposta_usuario)
            else:
                print("O número está acima de", resposta_usuario)
            valor1 -= 1
    print("Acabaram as tentativas")
    print("O número era:", numero_aleatorio)

elif escolha == 2:
    print("Você tem sete tentativas")
    while valor2 > 0:
        resposta_usuario = int(input("Digite um número: "))
        if resposta_usuario == numero_aleatorio:
            print("Você acertou")
            break
        else:
            print("Você errou")
            if resposta_usuario > numero_aleatorio:
                print("O número está abaixo de", resposta_usuario)
            else:
                print("O número está acima de", resposta_usuario)
            valor2 -= 1
    print("Acabaram as tentativas")
    print("O número era:", numero_aleatorio)

elif escolha == 3:
    print("Você tem cinco tentativas")
    while valor3 > 0:
        resposta_usuario = int(input("Digite um número: "))
        if resposta_usuario == numero_aleatorio:
            print("Você acertou")
            break
        else:
            print("Você errou")
            if resposta_usuario > numero_aleatorio:
                print("O número está abaixo de", resposta_usuario)
            else:
                print("O número está acima de", resposta_usuario)
            valor3 -= 1
    print("Acabaram as tentativas")
    print("O número era:", numero_aleatorio)

else:
    print("Valor incorreto")
