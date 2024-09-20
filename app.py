from modulo import *

if __name__ == "__main__":
    # Instância dos objetos
    endereco_pessoal = Endereco('', '', '', '')
    usuario = Pessoa('', 0, '','')
    telefone_pessoal = Telefone('','')

# Entrada de dados da pessoa
    usuario.nome = input('Informe o nome do usuário: ')
    usuario.idade = input('Informe sua idade: ')
    usuario.endereco = endereco_pessoal

    usuario.endereco = endereco_pessoal

    # Entrada de dados do endereço
    endereco_pessoal.cep = input('Informe o CEP: ')
    endereco_pessoal.uf = input('Informe a UF: ')
    endereco_pessoal.cidade = input('Informe a cidade: ')
    endereco_pessoal.bairro = input('Informe o bairro: ')

    usuario.telefone = telefone_pessoal


    # Entrada de dados do telefone
    ddd = input('Informe o DDD do telefone: ')
    numero = input('Informe o número do telefone: ')
    telefone_usuario = Telefone(ddd, numero)
    usuario.telefone = telefone_usuario

    # Saída de dados
    print(usuario.obter_info_pessoal())

