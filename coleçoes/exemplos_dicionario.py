pessoa = {'nome' : 'Goku', 
          'idade' : 43, 
          'sexo' : 'masculino'
        }
print(pessoa)

#ADD
pessoa['raça'] = 'sayajin'
pessoa['familia'] = ['Gohan', 'Goten', 'Chichi', 'Pan']

#UPDATE
pessoa['idade'] = 45

#DELETE
del pessoa['sexo']

#Acessando 'Chichi'
print(pessoa)
print(pessoa['familia'][2])



