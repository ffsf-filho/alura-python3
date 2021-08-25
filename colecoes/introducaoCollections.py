class IntroducaoCollections:
    idade1 = 39
    idade2 = 30
    idade3 = 27
    idade4 = 18
    print(idade1)
    print(idade2)
    print(idade3)
    print(idade4)

    idades = [39, 30, 27, 18]
    print(type(idades))
    print(idades)
    print(idades[2])
    print(len(idades))
    idades.append(15)
    print(idades)

    for idade in idades:
        print(idade)

    idades.remove(30)
    print(idades)

    idades.append(27)
    print(idades)
    idades.remove(27)
    print(idades)

    print(28 in idades)
    print(15 in idades)

    if 15 in idades:
        idades.remove(15)
    print(idades)

    idades.insert(0, 30)
    print(idades)

    idades.extend([15, 19])
    print(idades)

    idades_no_ano_que_vem = []
    for item in idades:
        idades_no_ano_que_vem.append(item + 1)
    print(idades_no_ano_que_vem)

    idades_no_ano_que_vem2 = [(item + 1) for item in idades]
    print(idades_no_ano_que_vem2)
    maior18 = [item for item in idades if item > 18]
    print(f'Maior 18 anos: {maior18}')

    #idades.clear()
    #print(idades)


if __name__ == "__main__":
    IntroducaoCollections()