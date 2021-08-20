import forca
import adivinhacao


def escolhe_jogo() -> object:
    print("*************************************")
    print("*        Escolha o seu Jogo         *")
    print("*************************************")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual Jogo? "))

    if jogo == 1:
        print("Jogando Forca!")
        forca.jogar()
    else:
        print("Jogando Adivinhação!")
        adivinhacao.jogar()


if __name__ == "__main__":
    escolhe_jogo()
