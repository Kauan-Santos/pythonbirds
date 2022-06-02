class Pessoa():
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        return f'Olá {self.nome}'


if __name__ == '__main__':
    p = Pessoa('Kauan', 22)
    print(Pessoa.cumprimentar(p))
    print(f'Nome: {p.nome}')
    print(f'Idade: {p.idade}')
