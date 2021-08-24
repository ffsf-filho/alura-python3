from testes import Testes
from extratorArgumentosURL import ExtartorArgumentosURL
from regex import Regex


class Main:
    Testes()

    print("\ntestes refernte a class ExtartorArumentosURL\n")

    url = "https://www.bytebank.com.br/cambio?Moedaorigem=real&moedadestino=dolar&valor=1500"
    url1 = "https://www.bytebank.com.br/cambio?Moedaorigem=real&moedadestino=dolar&valor=1500"
    url2 = None
    print(ExtartorArgumentosURL.url_eh_valida(url))

    argumentoUrl = ExtartorArgumentosURL(url)
    print(len(argumentoUrl))
    print(argumentoUrl)
    print(url == url1)
    moeda_origem, moeda_destino, valor_moeda = argumentoUrl.extrai_argumentos()
    print(f'{moeda_origem}, {moeda_destino}, {valor_moeda}')

    print("\ntestes referente a class Regex\n")

    email1 = "Meu número é 1234-1234"
    email2 = "Fale comigo em 1234-1234 esse é meu telefone 647859435"
    email3 = "91234-1234 é o meu celular e o do Antênio é 7894-6532 "

    Regex.extrai_telefone(email1)
    Regex.extrai_telefone(email2)
    Regex.extrai_telefone(email3)


if __name__ == '__main__':
    Main()