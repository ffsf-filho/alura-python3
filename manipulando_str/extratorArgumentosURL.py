class ExtartorArgumentosURL:
    def __init__(self, url):
        if self.url_eh_valida(url):
            self.url = url.lower()
        else:
            raise LookupError("Url invalida !!!!")

    def __len__(self):
        return len(self.url)

    def __str__(self):
        origem, destino, valor = self.extrai_argumentos()
        return f'Moeda de Origem: {origem}, Moeda de destino {destino} e o Valor: {valor}'

    def __eq__(self, outra_instancia):
        return self.url == outra_instancia.url


    @staticmethod
    def url_eh_valida(url):
        if url and url.startswith("https://www.bytebank.com.br"):
            return True
        else:
            return False

    def extrai_argumentos(self):
        origem = "moedaorigem=".lower()
        destino = "moedadestino=".lower()
        valor = "valor=".lower()

        moeda_origem = self.busca_moeda_origem(origem, destino)

        if moeda_origem == "moedadestino":
            self.troca_moeda_origem("moedadestino")
            moeda_origem = self.busca_moeda_origem(origem, destino)

        moeda_destino = self.busca_moeda_destino(destino, valor)

        valor_moeda = self.busca_valor(valor)

        return moeda_origem, moeda_destino, valor_moeda

    def encontra_indice_inicial(self, busca_moeda):
        return self.url.find(busca_moeda) + len(busca_moeda)

    def busca_moeda_origem(self, origem, destino):
        indice_inicial_moeda_origem = self.encontra_indice_inicial(origem)
        indice_final_moeda_origem = self.url.find(destino) - 1
        return self.url[indice_inicial_moeda_origem:indice_final_moeda_origem]

    def busca_moeda_destino(self, destino, valor):
        indice_inicial_moeda_destino = self.encontra_indice_inicial(destino)
        indice_final_moeda_destino = self.url.find(valor) - 1
        return self.url[indice_inicial_moeda_destino:indice_final_moeda_destino]

    def busca_valor(self, valor):
        indice_inicial_valor = self.encontra_indice_inicial(valor)
        return  self.url[indice_inicial_valor:]

    def troca_moeda_origem(self, moeda_origem):
        self.url = self.url.replace(moeda_origem, "real", 1)


if __name__ == '__main__':
    ExtartorArgumentosURL()
