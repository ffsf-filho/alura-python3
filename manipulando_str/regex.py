import re


class Regex:

    @staticmethod
    def extrai_telefone(texto):
        padrao = "[0-9]{4,5}[-]*[0-9]{4}"
        retorno = re.findall(padrao, texto)
        print(retorno)


if __name__ == '__main__':
    Regex()