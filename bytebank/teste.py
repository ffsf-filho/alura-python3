from decimal import Decimal
from conta import Conta
from datas import Data
from cliente import Cliente
from circulo import Circulo


def teste():
    conta1 = cria_conta(1234, "Francisco", Decimal("100.00"), Decimal("1000.00"))
    deposita(conta1, Decimal("12.33"))
    saca(conta1, Decimal("1.08"))
    extrato(conta1)

    conta2 = cria_conta(1228, "Josue", Decimal("100.00"), Decimal("1000.00"))
    saca(conta2, Decimal("32.18"))
    extrato(conta2)

    conta3 = Conta(1258, "Rodrigo", Decimal("158.00"), Decimal("1200.00"))
    conta3.deposita(Decimal("126.51"))
    conta3.extrato()

    conta4 = conta3
    conta3.saca(Decimal("10.25"))
    print("Extrato Conta 3")
    conta3.extrato()
    print("Extrato Conta 4")
    conta4.extrato()
    data = Data("21", "08", "2021")
    data.formatada()

    conta5 = Conta(1258, "Marcela", Decimal("900.00"), Decimal("2200.00"))
    conta3.transfere(conta5, Decimal("1274.26"))
    print("Extrato Conta 3")
    conta3.extrato()
    print("Extrato Conta 5")
    conta5.extrato()

    conta3.transfere(conta5, Decimal("200.00"))
    print("Extrato Conta 3")
    conta3.extrato()
    print("Extrato Conta 5")
    conta5.extrato()

    cliente = Cliente("robson")
    print(cliente.nome)
    cliente.nome = "alfredo"
    print(cliente.nome)

    conta3.limite = Decimal("8000.00")
    print(conta3.limite)
    conta3.extrato()

    print(f"PI = {Circulo.pi}")
def cria_conta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta


def deposita(conta, valor):
    conta["saldo"] += Decimal(valor)


def saca(conta, valor):
    conta["saldo"] -= Decimal(valor)


def extrato(conta):
    print(f"Titular: {conta['titular']}\nSaldo é R$ {Decimal(conta['saldo'])}\nSeu limite é R$ {Decimal(conta['limite'])}\n")


if __name__ == "__main__":
    teste()