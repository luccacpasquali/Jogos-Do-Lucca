import forca
import adivinhacao

print("******************")
print("Escolha o seu jogo")
print("******************"  )

print("[1] Forca [2] Adivinhação")
jogo = int(input("Digite sua escolha: "))

if(jogo == 1):
    print("Forca...")
    forca.jogar()
elif(jogo == 2):
    print("Adivinhação...")
    adivinhacao.jogar()
