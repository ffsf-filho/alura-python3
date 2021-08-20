import random


def jogar() -> object:
    print("*************************************")
    print("* Bem vindo ao jogo de adivinhação! *")
    print("*************************************")

    numero_secreto = round(random.randrange(1, 101))
    total_de_tentativas = 0
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")
    nivel = int(input("Defina o nível: "))

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print(f"Tentativa: {rodada}  de {total_de_tentativas}")
        chute_str = input("Digite o um número entre 1 e 100: ")
        chute = int(chute_str)
        print("Você digitou ", chute)

        if (chute < 1) or (chute > 100):
            print("Voce deve dgitar um número entre 1 e 100:")
            continue

        if numero_secreto == chute:
            print(f"Você acertou e fez {pontos} pontos!!!")
            break
        else:
            if numero_secreto < chute:
                print("Você errou. O seu chute foi maior do que o número secreto !!")
            elif numero_secreto > chute:
                print("Você errou. O seu chute foi menor do que o número secreto !!")

            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Fim do Jogo !")


if __name__ == "__main__":
    jogar()
