# #atividade 1
# class Pessoa:
#     def __init__(self, nome, idade, profissao):
#         self.nome = nome;
#         self.idade = idade;
#         self.profissao = profissao;
#     def prof(self):
#         return f"{self.nome} trabalha com {self.profissao}";
#     def aetas(self):
#         return f"{self.nome} terá {self.idade + 1} anos";
#     def __str__(self):                           
#         return f'Nome: {self.nome}, Idade: {self.idade}, {self.prof()} {self.aetas()}';

# pessoa1 = Pessoa('Reginaldo', 45, 'Contabilidade')

# print(str(pessoa1))

#atividade 2, 3, 4, 5
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular;
        self.saldo = saldo;
        self.ativo = False;
    
    def ativar_conta(self):
        if (self.ativo) == False: (self.ativo) == True
    
    def ativo(self):
        if (self.ativo == True):
            return f"A conta do titular {self.titular} está ativa"
        else:
            return f"A conta do titular {self.titular} está inativa"

    def __str__(self):
        return f'Titular: {self.titular}, Saldo: {self.saldo}'
    
conta = ContaBancaria("Reginaldo", 50000 )
print(str(f'O Saldo do titular {conta.titular} é de {conta.saldo}'))

#atividade 7, 8
class ClienteBanco:
    contass = []
    def __init__(self, nome, idade, estado, saldo, estado_civil):
        self.nome = nome
        self.idade = idade
        self.estado = estado
        self.saldo = saldo
        self.estado_civil = estado_civil
        ClienteBanco.contass.append(self)

    @classmethod
    def printar(cls):
        for i in cls.contass:
            print(f'Nome: {i.nome}, Idade: {i.idade}, Estado: {i.estado_civil}, Saldo: {i.saldo}, Estado_civil: {i.estado_civil}')

    def print(self):
        return f'Nome: {self.nome}, Idade: {self.idade}, Estado: {self.estado}, Saldo: {self.saldo}, Estado_civil: {self.estado_civil}'

cliente = ClienteBanco('Calabreso', 25, 'Acre', 10000000000000, "Solteiro")
cliente2 = ClienteBanco('Reginaldo', 45, 'Amapá', 50000, "Casado")
cliente3 = ClienteBanco('Eloir', 64, 'Paraná', 4000000, 'Casado')

print(ClienteBanco.printar())