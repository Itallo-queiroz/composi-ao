class Endereco:
    def __init__(self, cep, uf, cidade, bairro):
        self.__cep = cep
        self.__uf = uf
        self.__cidade = cidade
        self.__bairro = bairro

    @property
    def cep(self):
        return self.__cep

    @cep.setter
    def cep(self, cep):
        self.__cep = cep

    @property
    def uf(self):
        return self.__uf

    @uf.setter
    def uf(self, uf):
        self.__uf = uf

    @property
    def cidade(self):
        return self.__cidade

    @cidade.setter
    def cidade(self, cidade):
        self.__cidade = cidade

    @property
    def bairro(self):
        return self.__bairro

    @bairro.setter
    def bairro(self, bairro):
        self.__bairro = bairro

    def obter_endeco(self):
        return f"{self.__bairro}, cidade de {self.__cidade}, {self.__uf}. CEP: {self.cep}."


class Telefone:
    def __init__(self, ddd, numero):
        self.__ddd = ddd
        self.__numero = numero

    def obter_telefone(self):
        return f"({self.__ddd}) {self.__numero}"


class Pessoa:
    def __init__(self, nome, idade, endereco, telefone):
        self.__nome = nome
        self.__idade = idade
        self.__endereco = endereco
        self.__telefone = telefone

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade):
        self.__idade = idade

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

    def obter_info_pessoal(self):
        return f"{self.__nome}, {self.__idade} anos, mora em {self.__endereco.obter_endeco()}. Telefone: {self.__telefone.obter_telefone()}."




