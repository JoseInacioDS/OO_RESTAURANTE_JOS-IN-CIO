#atividade 1

class carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo;
        self.cor = cor;
        self.ano = ano;

Nissan = carro("Skyline GTR R34", "Azul", 1998);
print(Nissan);

#atividade 2

restaurante = [];

class restaurante:
        nome = "";
        categoria = "";
        ativo = False;
        localizacao = "";
        horario = "";

Madaloso = restaurante();

Madaloso.nome = "Madaloso";
Madaloso.categoria = "Churrascaria";
Madaloso.localizacao = "São José Dos Pinhais";
Madaloso.horario = "11:30 às 15:00";
print(Madaloso);

#atividade 3

class restaurantes:
    def __init__(self, nome, categoria, localizacao, horario):
        self.nome = nome;
        self.categoria = categoria;
        self.ativo = False;
        self.localizacao = localizacao;
        self.horario = horario;

Mcdonalds = restaurantes ("Mcdonalds", "Fast-Food", "Campo-Largo", "24h");
print(Mcdonalds);

#atividade 4
class restaurant:
    def __init__(self, nome, categoria, localizacao, horario):
        self.nome = nome;
        self.categoria = categoria;
        self.ativo = False;
        self.localizacao = localizacao;
        self.horario = horario;
    def __str__(self):
        return(f"restaurante :{self.nome}, categoria: {self.categoria}, localização: {self.localizacao}, Horário de atendimento: {self.horario}");

BurgerKing = restaurant ("Burger King", "Fast-Food", "Campo-Largo", "24h");
print(BurgerKing);

#atividade 5
    
class Cliente: 
    def __init__(self, nome, idade, altura, cabelo):
        self.nome = nome;
        self.idade = idade;
        self.altura = altura;
        self.cabelo = cabelo;
    def __str__(self):
        return(f"nome: {self.nome}, idade: {self.idade}, altura: {self.altura}, cabelo: {self.cabelo}")

Allan_de_Castro = Cliente ("Allan de Castro", 17, 1.67, "castanho escuro");

Marion_Carolini = Cliente ("Marion Carolini", 16,  1.63, "preto");

Agatha = Cliente ("Agatha", 35, 1.98, "roxo escuro");

print(Allan_de_Castro, Marion_Carolini, Agatha);
