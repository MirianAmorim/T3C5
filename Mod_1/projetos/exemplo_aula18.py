class Funcionario:
    def __init__(self, nome, cargo, valor_hora_trabalhada):
        self.nome = nome
        self.cargo = cargo
        self.valor_hora_trabalhada = valor_hora_trabalhada
        self.__horas_trabalhadas = 0
        self.__salario = 0
        
    @property    
    def salario(self):
       return self.__salario
        

    def registra_hora_trabalhada(self):
        self.__horas_trabalhadas += 1

    def calcula_salario(self):
        self.__salario = self.__horas_trabalhadas * self.valor_hora_trabalhada
    
mirian = Funcionario("mirian","dev senior", 100)
# print(vars(mirian))
mirian.registra_hora_trabalhada()
mirian.registra_hora_trabalhada()
mirian.registra_hora_trabalhada()
mirian.registra_hora_trabalhada()
mirian.registra_hora_trabalhada()
mirian.calcula_salario()
# print(vars(mirian))
print(mirian.salario)