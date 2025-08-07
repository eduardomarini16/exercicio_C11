conjunto = {"Goku", "Vegeta", "Trunks", "Gohan"} # não guarda a ordem dos elementos
print(conjunto)

#Adicionar elementos
conjunto.add('Bulma')
conjunto.add('Goku') #não permite adicionar elementos repetidos
print(conjunto)

#Remover elementos
conjunto.remove('Trunks')
print(conjunto)

#Descobrir tipo
print(type(conjunto))