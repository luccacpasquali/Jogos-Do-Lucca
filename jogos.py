import time

import forca
import adivinhacao

def escolha_jogo():
    jogo = 0

    print("******************")
    print("Escolha o seu jogo")
    print("******************")

    while jogo != 3:
        print("\n[1] Forca [2] Adivinhação [3] Sair")
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
            print("Até logo...")
        else:
            print("--- ERRO ---")
            print("Número inváldo :( Tente novamete!")



escolha_jogo()
