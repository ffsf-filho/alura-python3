class Programa:
    def __init__(self, nome, ano):
        self.__nome = nome.title()
        self.ano = ano
        self.__likes = 0

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome.title()

    @property
    def like(self):
        return self.__likes

    def dar_like(self):
        self.__likes += 1

    def __str__(self):
        return f'Nome: {self.nome} - Ano: {self.ano} - Likes: {self.like}'
