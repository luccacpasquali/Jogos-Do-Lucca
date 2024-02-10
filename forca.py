import random
import bem_vindo

def jogar():
    bem_vindo.bem_vindo_jogo("Forca")

    palavra_secreta = carrega_palavras()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0

    while (not enforcou and not acertou):
        chute = pede_chute()

        if (chute in palavra_secreta):
            marca_chute_certo(palavra_secreta, chute, letras_acertadas)
        else:
            erros += 1
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        imprime_menssagem_vencedor()
    else:
        imprime_menssagem_perdedor(palavra_secreta)


def imprime_bem_vindo():
    print("***********************")
    print("Bem vindo ao jogo Forca")
    print("***********************")


def carrega_palavras():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()

    palavra_secreta = palavras[random.randrange(0, len(palavras))].upper()

    return palavra_secreta


def inicializa_letras_acertadas(palavra_secreta):
    return ["_" for letra in palavra_secreta]


def pede_chute():
    chute = input("Digite seu seu chute: ")
    chute = chute.strip().upper()
    return chute


def marca_chute_certo(palavra_secreta, chute, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = chute
        index += 1


def imprime_menssagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def imprime_menssagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \\       ")
    print("  /                 \\      ")
    print("//                   \\/\\  ")
    print("\\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \\__      XXX      __/     ")
    print("   |\\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \\_             _/       ")
    print("     \\_         _/         ")
    print("       \\_______/           ")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if (erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (erros == 2):
        print(" |      (_)   ")
        print(" |      \\     ")
        print(" |            ")
        print(" |            ")

    if (erros == 3):
        print(" |      (_)   ")
        print(" |      \\|    ")
        print(" |            ")
        print(" |            ")

    if (erros == 4):
        print(" |      (_)   ")
        print(" |      \\|/   ")
        print(" |            ")
        print(" |            ")

    if (erros == 5):
        print(" |      (_)   ")
        print(" |      \\|/   ")
        print(" |       |    ")
        print(" |            ")

    if (erros == 6):
        print(" |      (_)   ")
        print(" |      \\|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \\|/   ")
        print(" |       |    ")
        print(" |      / \\   ")

    print(" |            ")
    print("_|___         ")
    print()


if (__name__ == "__main__"):
    jogar()
