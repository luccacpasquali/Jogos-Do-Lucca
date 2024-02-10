def jogar( ):
    import random

    print("*********************************")
    print("Bem vindo ao jogo de adivinhação")
    print("*********************************")

    numero_secreto = round(random.randrange(1,101))
    total_tentativas = 0
    pontos = 1000

    print("Qual nivel deseja jogar?")
    nivel = int(input("[1] Fácil [2] Médio [3] Difícil: "))

    if(nivel == 1):
        total_tentativas = 20
    elif(nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5

    for rodada in range(1,total_tentativas + 1):
        print("Tentativa: {} de {}".format(rodada,total_tentativas))

        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou ",chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Número Inválido, você deve jogar um número entre 1 e 100")
            continue

        acertou    = chute == numero_secreto
        chuteMenor = chute > numero_secreto

        if(acertou):
            print("Você acertou e fez {} pontos".format(pontos))
            break
        else:
            print("Você errou")
            if(chuteMenor):
                print("O número secreto é MENOR que seu chute")
            else:
                print("O número secreto é MAIOR que seu chute")

            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Fim de Jogo!")
    print(numero_secreto)

if(__name__ == "__main__"):
    jogar()
