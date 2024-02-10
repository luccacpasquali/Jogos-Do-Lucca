def bem_vindo_jogo(nome_jogo):
    asteriscos_palavra = ''.join('*' for letra in nome_jogo)
    print("*******************{}".format(asteriscos_palavra))
    print("Bem vindo ao jogo {}".format(nome_jogo))
    print("*******************{}".format(asteriscos_palavra))

bem_vindo_jogo("adivinhação")