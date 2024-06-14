class livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True


    def disponivel(self):
        return('Disponivel') if self. disponivel == True else ('indisponivel')

   
    def __str__(self):
        return f'Título: {self.titulo}, Autor: {self.autor}, Ano de Publicação {self.ano_publicacao}'


    @staticmethod
    def verificar_disponibilidade(ano, livros):
        return [livro for livro in livros if livro.ano_publicacao == ano and livro.disponivel]

livro1 = livro ('As Longas Tranças do Rei Careca', 'Allan', 3048)
livro2 = livro ('Poeira em Alto Mar', 'Jose', 1972)
livro3 = livro ('Allan e seus Hollows Nights', 'Allan', 1852)

livros = [livro1, livro2, livro3]
disponiveis_3048 = livro.verificar_disponibilidade(3048, livros)
print(disponiveis_3048)