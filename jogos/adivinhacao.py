print("*********************************")
print("Bem vindo ao jogo de advinhação!")
print("*********************************")

numero_secreto = 42
total_de_tentativas = 3

for rodada in range(1, total_de_tentativas + 1):
    print(f"Tentativa: {rodada}  de {total_de_tentativas}")
    chute_str = input("Digite o seu nuúmero! ")
    chute = int(chute_str)
    print("Você digitou ", chute)

    if numero_secreto == chute:
        print("Você acertou !!!")
        break
    elif numero_secreto < chute:
        print("Você errou. O seu chute foi maior do que o número secreto !!")
    else:
        print("Você errou. O seu chute foi menor do que o número secreto !!")

print("Fim do Jogo !")