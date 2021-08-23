from programa import Programa


class Serie(Programa):
    def __init__(self, nome, ano, temporada):
        super().__init__(nome, ano)
        self.temporada = temporada

    def __str__(self):
        return f'Nome: {self.nome} - Ano: {self.ano} - Temporada(s): {self.temporada} - Likes: {self.like}'
