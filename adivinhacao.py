import bem_vindo
def jogar( ):
    import random

    #inicia o jogo com saudação
    bem_vindo.bem_vindo_jogo("Adivinhação")

    numero_secreto = round(random.randrange(1,101))
    total_tentativas = escolha_nivel()
    pontos = 1000

    #roda o jogo enquanto tiver tentativas
    for rodada in range(1,total_tentativas + 1):
        print("Tentativa: {} de {}".format(rodada,total_tentativas))

        #recebe o chute do usuario
        chute = int(input("Digite um número entre 1 e 100: "))

        print("Você digitou ",chute)

        #valida chute do usurio
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
    if not acertou:
        print("O número secreto era {}".format(numero_secreto))

# recebe o nível que o usuario quer jogar e retorna  o numero de tentativas
def escolha_nivel():
    print("Qual nivel deseja jogar?")
    nivel = int(input("[1] Fácil [2] Médio [3] Difícil: "))

    if (nivel == 1):
        total_tentativas = 20
    elif (nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5

    return total_tentativas

if(__name__ == "__main__"):
    jogar()
