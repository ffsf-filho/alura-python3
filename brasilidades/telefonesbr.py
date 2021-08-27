import re


class TelefonesBr:
    def __init__(self, telefone):
        if self.__valida(telefone):
            padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
            resposta = re.search(padrao, telefone)
            self.__telefone = f"+{resposta.group(1)} ({resposta.group(2)}) {resposta.group(3)}-{resposta.group(4)}"
        else:
            raise  ValueError("Número incorreto!!")

    def __str__(self):
        return self.__telefone

    def __valida(self, telefone):
        padrao = "[0-9]{2,3}[0-9]{2}[0-9]{4,5}[0-9]{4}"
        resposta = re.findall(padrao, telefone)

        if resposta:
            return True
        else:
            return False
