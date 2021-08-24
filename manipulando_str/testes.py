class Testes:
    print("testes referente a class Testes\n")

    sobre_mim = "Meu nome é Rodrigo e minha idade é 26"
    meu_nome = "Rodrigo"

    sub_string = meu_nome[4]
    print(sub_string)

    sub_string = meu_nome[2:6]
    print(sub_string)

    sub_string = sobre_mim[35:]
    print(sub_string)

    url = "https://www.bytebank.com.br/cambio?moedaorigem=real&moedadestino=dolar&valor=1500"
    argumento = "moedaorigem=real"
    sub_string = argumento[:11]
    print(sub_string)

    index = argumento.find("=")
    sub_string = argumento[index + 1:]
    print(sub_string)

    sub_string = argumento.split("=")
    print(sub_string)

    string_vazia = ""
    print(string_vazia is None)
    string_nula = None
    print(string_nula is None)

    def valida_string(texto):

        if texto:
            return print("Tem algo aqui")
        else:
            return print("Não tem algo aqui")

    valida_string(string_nula)
    valida_string(sub_string)
    valida_string(string_vazia)


if __name__ == '__main__':
    Testes()
