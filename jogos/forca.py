import os.path
import random





def jogar() -> object:
    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()
    palavra = inicializa_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    erro = 0

    while (not enforcou) and (not acertou):
        print(f"Têm {len(palavra)} letras, a palvra é: {palavra}")
        chute = pede_chute()

        if chute in palavra_secreta:
            marca_chute_correto(chute, palavra_secreta, palavra)
        else:
            erro += 1
            desenha_forca(erro)
            print("Ops, você errou! Faltam {} tentativas.".format(7 - erro))

        enforcou = erro == 7
        acertou = "_" not in palavra

    resultado(acertou, palavra, palavra_secreta)


def imprime_mensagem_abertura():
    print("*************************************")
    print("*    Bem vindo ao jogo de Forca!    *")
    print("*************************************")


def carrega_palavra_secreta():
    if os.path.exists("palabras.txt").__doc__:
        with open("palavras.txt", "r+") as arquivo:
            linhas = arquivo.read().split()

            if not "jaboticaba" in linhas:
                arquivo.write("jaboticaba\n")
    else:
        with open("palavras.txt", "w+") as arquivo:
            arquivo.write("maça\n")

    with open("palavras.txt", "r") as arquivo:
        lista_palavras = arquivo.read().split()

    indice_palavra = round(random.randrange(0, len(lista_palavras)))
    palavra_secreta = lista_palavras[indice_palavra].lower()

    return palavra_secreta


def inicializa_letras_acertadas(palavra_secreta):
    return ["_" for letra in palavra_secreta]


def pede_chute():
    chute = input("Qual letra? ")
    return chute.strip().lower()


def marca_chute_correto(chute, palavra_secreta, palavra):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            palavra[index] = chute
        index += 1


def resultado(acertou, palavra, palavra_secreta):
    if acertou:
        print(f"Parabéns! Você acertou ! a plavra é {palavra} .")
        imagem_taca()
    else:
        print(f"Que pena! Você errou e foi enforcado ! a plavra era {palavra_secreta} .")
        imagem_caveira()


def imagem_caveira():
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def imagem_taca():
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


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
            print(" |      (_)   ")
            print(" |            ")
            print(" |            ")
            print(" |            ")
    if(erros == 2):
            print(" |      (_)   ")
            print(" |      \     ")
            print(" |            ")
            print(" |            ")
    if(erros == 3):
            print(" |      (_)   ")
            print(" |      \|    ")
            print(" |            ")
            print(" |            ")
    if(erros == 4):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |            ")
            print(" |            ")
    if(erros == 5):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |            ")
    if(erros == 6):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |      /     ")
    if (erros == 7):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |      / \   ")
    print(" |            ")
    print("_|___         ")
    print()


if __name__ == "__main__":
    jogar()