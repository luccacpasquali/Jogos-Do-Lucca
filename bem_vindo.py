def bem_vindo_jogo(nome_jogo):
    asteriscos_palavra = ''.join('*' for letra in nome_jogo)
    print("\n*******************{}".format(asteriscos_palavra))
    print("Bem vindo ao jogo {}".format(nome_jogo))
    print("*******************{}\n".format(asteriscos_palavra))
