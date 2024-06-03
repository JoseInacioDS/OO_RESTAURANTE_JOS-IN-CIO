class restaurante:
    nome=''
    categoria=''
    ativo= False


restaurante_praca = restaurante()
restaurante_praca.nome = 'Praça'

#Questão 5
restaurante_praca.nome = 'Bistrô'

#Questão 1
restaurante_praca.categoria = 'Italiana'

restaurante_pizza = restaurante()

#Questão 6
restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast-Food'
#Questão 8
restaurante_pizza.ativo = 'Ativo'

#Questão 2
print(restaurante_praca.nome)

#Questão 3
if restaurante_praca.ativo == True:
    print('O restaurante está Ativo')
else:
    print('O restaurante está Inativo')

#Questão 4
print(restaurante_praca.categoria)
categoria = restaurante_praca.categoria

#Questão 7
if restaurante_pizza.categoria == "Fast-Food":
    print('O restaurante é Fast-Food')
else:
    print('O restaurante não é Fast-Food')

#Questão 9
print(vars(restaurante_praca))
