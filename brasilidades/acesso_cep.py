import requests

class BuscaEndereco:
    def __init__(self, cep):
        cep = str(cep)

        if self.__cep_eh_valido(cep):
            self.__cep = cep
        else:
            raise ValueError("CEP inválido!!")

    def __str__(self):
        return self.__format_cep()

    def __cep_eh_valido(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False

    def __format_cep(self):
        return f'CEP: {self.__cep[:5]}-{self.__cep[5:]}'

    def acessa_via_cep(self):
        url = f"https://viacep.com.br/ws/{self.__cep}/json/"
        resposta = requests.get(url).json()
        return (resposta['bairro'], resposta['localidade'], resposta['uf'])
