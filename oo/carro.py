"""
Você deve criar uma classe carro que vai possuir dois atributos compostos por outras duas classes:
1) Motor
2) Direção

O motor terá a responsabilidade de controloar a velocidade.
Ele oferece os seguintes atributos:
1) Atributo de dado velocidade.
2) Metodo acelerar, que devera incrementar a velocidade de uma unidade.
3) Metodo frear, que devera decrementar a velocidade em duas unidades.

A direção terá a responsabilidade de controlar a direção. Ela oferece os seguintes atributos:
1) Valor de direção com valores possiveis: Norte, sul, leste e Oeste.
2) Método girar a direita.
3) Método girar a esquerda

Exemplo:
# Testando Velocidade
>>> motor = Motor()
>>> motor.velocidade
0
>>> motor.acelerar()
>>> motor.velocidade
1
>>> motor.acelerar()
>>> motor.velocidade
2
>>> motor.acelerar()
>>> motor.velocidade
3
>>> motor.frear()
>>> motor.velocidade
1
>>> motor.frear()
>>> motor.velocidade
0

# Testando Direção
>>> direcao = Direcao()
>>> direcao.valor
'Norte'
>>> direcao.girar_a_direita()
>>> direcao.valor
'Leste'
>>> direcao.girar_a_direita()
>>> direcao.valor
'Sul'
>>> direcao.girar_a_direita()
>>> direcao.valor
'Oeste'
>>> direcao.girar_a_direita()
>>> direcao.valor
'Norte'
>>> direcao.girar_a_esquerda()
>>> direcao.valor
'Oeste'
>>> direcao.girar_a_esquerda()
>>> direcao.valor
'Sul'
>>> direcao.girar_a_esquerda()
>>> direcao.valor
'Leste'
>>> direcao.girar_a_esquerda()
>>> direcao.valor
'Norte'

# Testando Carro
>>> carro = Carro(direcao, motor)
>>> carro.calcula_velocidade()
0
>>> carro.acelerar()
>>> carro.calcular_velocidae()
1
>>> carro.acelerar()
>>> carro.calcular_velocidae()
2
>>> carro.frear()
>>> carro.calcular_velocidae()
0
>>> carro.calcular_direcao()
'Norte'
>>> carro.girar_a_direita()
>>> carro.calcular_direcao
'Leste'
>>> carro.girar_a_esquerda()
>>> carro.calcular_direcao()
'Norte'
>>> carro.girar_a_esquerda()
>>> carro.calcular_direcao()
'Oeste'
"""


class Carro():

    def __init__(self, motor, direcao):
        self.motor = motor
        self.direcao = direcao


    def calcular_velocidade(self):
        return self.motor.velocidade


    def calcular_direcao(self):
        return self.direcao.direcao


    def acelerar(self):
        self.motor.acelerar()


    def frear(self):
        self.motor.frear()


    def girar_a_direita(self):
        self.direcao.girar_a_direita()


    def girar_a_esquerda(self):
        self.direcao.girar_a_esquerda()
        

class Motor:

    def __init__(self):
        self.velocidade = 0

    
    def acelerar(self):
        self.velocidade += 1
        

    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)

NORTE = 'Norte'
SUL = 'Sul'
LESTE = 'Leste'
OESTE = 'Oeste'

class Direcao:


    rotacao_a_direita_dct = {
        NORTE: LESTE, LESTE: SUL, SUL: OESTE, OESTE: NORTE
    }
    rotacao_a_esquerda_dct = {
        NORTE: OESTE, LESTE: NORTE, SUL: LESTE, OESTE: SUL
    }

    def __init__(self):
        self.direcao = NORTE

    
    def girar_a_esquerda(self):
        self.direcao = self.rotacao_a_esquerda_dct[self.direcao]


    def girar_a_direita(self):
        self.direcao = self.rotacao_a_direita_dct[self.direcao]



motor_do_carro = Motor()
direcao_do_carro = Direcao()
carro = Carro(motor_do_carro, direcao_do_carro)
print(carro.calcular_direcao())
print(carro.calcular_velocidade())

motor_do_carro.acelerar()
motor_do_carro.acelerar()
motor_do_carro.acelerar()
motor_do_carro.acelerar()
motor_do_carro.acelerar()

direcao_do_carro.girar_a_direita()

print(carro.calcular_velocidade())
print(carro.calcular_direcao())
