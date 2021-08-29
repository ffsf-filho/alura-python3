from src.excecoes import LanceInvalido


class Usuario:

    def __init__(self, nome, carteira):
        self.__nome = nome
        self.__carteira = carteira

    def propoe_lance(self, leilao, valor):
        if not self.__valor_eh_valido(valor):
            raise LanceInvalido("Não pode propor um lance com o valor maior que o valor da carteira")

        lance = Lance(self, valor)
        leilao.propoe(lance)

        self.__carteira -= valor

    @property
    def nome(self):
        return self.__nome

    @property
    def carteira(self):
        return self.__carteira

    def __valor_eh_valido(self, valor):
        return valor <= self.__carteira


class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor


class Leilao:

    def __init__(self, descricao):
        self.descricao = descricao
        self.__lances = []
        self.maior_lance = 0.0
        self.menor_lance = 0.0

    def propoe(self, lance: Lance):
        if self.lance_eh_valido(lance):
            if not self.__tem_laces():
                self.menor_lance = lance.valor

            self.maior_lance = lance.valor
            self.__lances.append(lance)

    @property
    def lances(self):
        return self.__lances[:]

    def __tem_laces(self):
        return self.__lances

    def __usuarios_diferentes(self, lance):
        if self.__lances[-1].usuario != lance.usuario:
            return True

        raise LanceInvalido('O mesmo usuário não pode dar dois lances seguidos.')


    def __valor_maior_que_lance_anterior(self, lance):
        if lance.valor > self.__lances[-1].valor:
            return True

        raise LanceInvalido('O valor do lance deve ser maior que o do lance anterior.')

    def lance_eh_valido(self, lance):
        return not self.__tem_laces() or (self.__usuarios_diferentes(lance) and
                                          self.__valor_maior_que_lance_anterior(lance))
