lista = ["Goku", "Vegeta", "Trunks", "Gohan"]
#Mostrar elementos da lista
print(lista)

#Inserir elementos
lista.append('Bulma') # adiciona no fim da lista
lista.insert(1, 'Kuririm') # adiciona no índice desejado
print(lista)

#Alterando elementos
lista[0] = 'Piccolo'
print(lista)

#Excluindo elementos
del lista[0] # remoção pelo índice
lista.remove('Bulma') # remoção por valor
print(lista)