import time
import bem_vindo
import random

def jogar():
    bem_vindo.bem_vindo_jogo("Jokenpo")
    inicio_jokenpo()

    codigo = random.randrange(1, 3)
    usuario = escolha_do_usurario()

    imprime_escolhas(codigo,usuario)
    calculando_resultado(usuario,codigo)


def inicio_jokenpo():
    inicio = int(input("[1] Iniciar [2] Regras: \n"))
    if (inicio == 2):
        print("********* Regras *********\n")
        print("Você deve escolher entre Pedra, Papel ou Tesoura")
        print("O código é seu adversário")
        print("Ele vai escolher aleatoriamente entre um dos três")
        print("A procedência do jogo é a seguinte: \n")
        print("Pedra ganha de Tesoura")
        print("Papel ganha de Pedra")
        print("Tesoura ganha de Papel")
        print("\n**************************")
        time.sleep(2)
        input("\nAperte ENTER para iniciar\n")

def escolha_do_usurario():
    escolha_do_usurario = int(input("[1] Pedra [2] Papel [3] Tesoura: \n"))
    return escolha_do_usurario

def imprime_escolhas(codigo,usuario):
    codigo_str = escolha_str(codigo)
    usuario_str = escolha_str(usuario)

    print("Calculando resultado...")
    time.sleep(2)
    print("A sua escolha foi: {}".format(usuario_str))
    print("A escolha do cumputador foi: {}\n".format(codigo_str))


def escolha_str(player):
    if(player == 1):
        str = "pedra"
    elif(player == 2):
        str = "papel"
    else:
        str = "tesoura"
    return str


def calculando_resultado(usuario, codigo):

    nome_usuario = "você"
    nome_código = "o código"

    #1(pedra) ganha 3(tesoura)
    #3(tesoura) ganha 2(papel)
    #2(papel) ganha 1(pedra)

    # se usuario escolheu pedra
    if (usuario == 1):
        # SE CODIGO ESCOLHEU PEDRA
        if (codigo == 1):
            empate(usuario)
        # SE CODIGO ESCOLHEU PAPEL
        elif (codigo == 2):
            vitoria_papel(nome_código, nome_usuario)
        # SE CODIGO ESCOLHEU TESOURA
        else:
            vitoria_pedra(nome_usuario, nome_código)

    # SE USUARIO ESCOLHEU PAPEL
    elif (usuario == 2):
        # CODIGO ESCOLHEU PEDRA
        if (codigo == 1):
            vitoria_papel(nome_usuario, nome_código)
        # SE CODIGO ESCOLHEU PAPEL
        elif (codigo == 2):
            empate(usuario)
        # SE CODIGO ESCOLHEU TESOURA
        else:
            vitoria_tesoura(nome_código, nome_usuario)

    # SE USUARIO ESCOLHEU TESOURA
    else:
        # CODIGO ESCOLHEU PEDRA
        if (codigo == 1):
            vitoria_pedra(nome_código, nome_usuario)
        # SE CODIGO ESCOLHEU PAPEL
        elif (codigo == 2):
            vitoria_tesoura(nome_usuario, nome_código)
        # SE CODIGO ESCOLHEU TESOURA
        else:
            empate(usuario)


def empate(escolha):
    if(escolha == 1):
        print("\nA batalha foi dura mas terminiu em empate")
    elif(escolha == 2):
        print("A batalha foi tão leve que empatou")
    else:
        print("A batalha foi afiada mas terminiu em empate")


def vitoria_pedra(ganhador,perdedor):
    print("{} amassou {} e levou a vitoria".format(ganhador,perdedor))

def vitoria_papel(ganhador,perdedor):
    print("{} imobilizou {} e garantiu a vitoria".format(ganhador,perdedor))

def vitoria_tesoura(ganhador,perdedor):
    print("{} com facilidade despedaçou {} e levou a vitoria".format(ganhador,perdedor))


if(__name__ == "__main__"):
    jogar()
