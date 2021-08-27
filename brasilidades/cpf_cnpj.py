from validate_docbr import CPF, CNPJ


class Documento:
    @staticmethod
    def cria_documento(documento):
        documento = str(documento)

        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError("Quantidade de digitos esta incorreta !!")


class DocCpf:
    def __init__(self, documento):
        if self.valida(documento):
            self.__cpf = documento
        else:
            raise ValueError("Cpf inválido!!")

    def __str__(self):
        return self.format()

    def valida(self, documento):
        validador = CPF()
        return validador.validate(documento)

    def format(self):
        mascara = CPF()
        return mascara.mask(self.__cpf)


class DocCnpj:
    def __init__(self, documento):
        if self.valida(documento):
            self.__cnpj = documento
        else:
            raise ValueError("Cnpj inválido!!")

    def __str__(self):
        return self.format()

    def valida(self, documento):
        validador = CNPJ()
        return validador.validate(documento)

    def format(self):
        mascara = CNPJ()
        return mascara.mask(self.__cnpj)
