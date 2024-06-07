

class Restaurantes:
    restaurantes = []
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self._ativo = False
        Restaurantes.restaurantes.append(self)

    def __str__(self):
        return (f"Nome: {self.nome}, Categoria: {self.categoria}, Ativo:")

    @property
    def ativo(self):
        return('✅') if self._ativo == True else '❌'

    @classmethod
    def listar(cls):
        print(f'{"Nome do Restaurante"}, {"Categoria"}, {"Status"}')
        for restauranteD in cls.restaurantes:
            print(f'{restauranteD.nome.ljust(20)}, {restauranteD.categoria.ljust(20)}, {restauranteD.ativo}')
    
restPraca = Restaurantes('Praça', 'praça')
restPizza = Restaurantes('Pizza', 'pizza')

print(Restaurantes.listar())