import time
import forca
import adivinhacao
import jokenpo

def escolha_jogo():
    jogo = 0

    print("***************")
    print("Jogos do Lucca")
    print("    ʕ•́ᴥ•̀ʔっ    ")
    print("***************")

    while jogo != 3:
        print("\n[1] Forca [2] Adivinhação [3] Jokenpô [4] Sair")
        jogo = int(input("Digite sua escolha: "))

        if (jogo == 1):
            print("Forca...")
            time.sleep(2)
            forca.jogar()
        elif (jogo == 2):
            print("Adivinhação...")
            time.sleep(2)
            adivinhacao.jogar()
        elif (jogo == 3):
            print("Adivinhação")
            jokenpo.jogar()
        elif(jogo == 4):
            print("Até logo...")
            time.sleep(4)
        else:
            print("--- ERRO ---")
            print("Número inváldo :( Tente novamete!")



escolha_jogo()
