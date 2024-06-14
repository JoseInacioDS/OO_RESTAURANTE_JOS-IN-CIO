from atividade4 import livro

livro1 = livro ('As Longas Tranças do Rei Careca', 'Allan', 3048)
livro2 = livro ('Poeira em Alto Mar', 'Jose', 1972)
livro3 = livro ('Allan e seus Hollows Nights', 'Allan', 1852)

livros = [livro1, livro2, livro3]
disponiveis_3048 = livro.verificar_disponibilidade(3048, livros)
print(disponiveis_3048)