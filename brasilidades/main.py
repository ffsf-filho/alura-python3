from cpf_cnpj import Documento
from telefonesbr import TelefonesBr
from datas_br import DatasBr
from  acesso_cep import BuscaEndereco

cpf = 15316264754
cnpj = 35379838000112

documento_cpf = Documento.cria_documento(cpf)
print(f'CPF: {documento_cpf}')

documento_cnpj = Documento.cria_documento(cnpj)
print(f'CNPJ: {documento_cnpj}')

telefone = "552126481234"
telefone_objeto = TelefonesBr(telefone)
print(telefone_objeto)

cadastro = DatasBr()
print(cadastro.momento_cadastro)
print(cadastro.mes_cadastro())
print(cadastro.dia_semana())
print(cadastro)
print(cadastro.tempo_cadastro())

cep = '01001000'
objeto_cep = BuscaEndereco(cep)
print(objeto_cep)
dados = objeto_cep.acessa_via_cep()
print(dir(dados))
print(dados)
