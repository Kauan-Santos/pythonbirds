class Pessoa():

    olhos = 2

    def __init__(self, *filhos, nome_completo=None, idade=None):
        self.nome_completo = nome_completo
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {self.nome_completo}'


if __name__ == '__main__':
    Kauan = Pessoa(nome_completo='Altieres Kauan dos Santos')
    Gessica = Pessoa(nome_completo='Gessica Dos Santos')
    Dinael = Pessoa(nome_completo='Dinael dos Santos')
    Dinael.cidade = 'Campo Limpo Paulista'
    Jose = Pessoa(Kauan, Gessica, nome_completo='José Vantuil dos Santos', idade=55)
    print(Pessoa.cumprimentar(Jose))
    print(f'Nome: {Jose.nome_completo}')
    print(f'Idade: {Jose.idade}')
    for filho in Jose.filhos:
        print(f'Filhos: {filho.nome_completo}')
    print(Kauan.__dict__)
    print(Dinael.__dict__)
    del Dinael.cidade
    print(Dinael.__dict__)
    print(Dinael.olhos)