from decimal import Decimal


class Conta:

    def __init__(self, numero, titular, saldo=Decimal("0.0"), limite=Decimal("1000.00")):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def __disponivel(self):
        if Decimal(self.__saldo) <= Decimal("0.00"):
            return Decimal(self.__limite)

        return Decimal(self.__saldo) + Decimal(self.__limite)

    def extrato(self):
        print(f"Titular: {self.__titular}\nSaldo é R$ {Decimal(self.__saldo)}\nSeu limite é R$ {Decimal(self.__limite)}\n")

    def deposita(self, valor=Decimal("0.0")):
        self.__saldo += Decimal(valor)

    def saca(self, valor=Decimal("0.0")):
        disponivel = self.__disponivel()

        if Decimal(disponivel) >= Decimal(valor):
            if Decimal(self.__saldo) >= Decimal(valor):
                self.__saldo -= Decimal(valor)
            else:
                if Decimal(self.__saldo) <= Decimal("0.00"):
                    self.__limite = Decimal("0.00")
                    self.__saldo -= valor
                else:
                    valor_deducao = (Decimal(valor) - Decimal(self.__saldo))
                    self.__limite -= valor_deducao
                    self.__saldo = -valor_deducao

            return True
        else:
            return False

    def transfere(self, destino,  valor = Decimal('0.0')):
        if self.saca(Decimal(valor)):
            destino.deposita(Decimal(valor))
            print(f"Valor R$ {Decimal(valor)} transferido com sucesso !")
        else:
            print("Não é possível a transferência, saldo insuficiente.")

    @property
    def _saldo(self):
        return Decimal(self.__saldo)
    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return Decimal(self.__limite)

    @limite.setter
    def limite(self, limite = Decimal("1000.00")):
        self.__limite = Decimal(limite)

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}