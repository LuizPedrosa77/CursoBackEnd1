
# Lista manual
lista = ['Maria', 23, 'Porto Alegre']
print(lista[0])
print(lista[1])
print(lista[2])

# Elementos sendo acessados individualmente
n = lista.index('Porto Alegre')
print(n)

# [2] -> Acessando o terceiro elemento da lista e [1] -> acessando o segundo elemento da lista
lista = ['Maria', 23, ['Porto Alegre', 'Rio de Janeiro']]
print(lista[2][0]) #Porto Alegre
print(lista[2][1]) #Rio de Janeiro

# Alterando um elemento da lista
lista = ['Maria', 23, ['Porto Alegre', 'Rio de Janeiro']]
lista[0] = 'Luiz'
lista[1] = 33
lista[2][0] = 'Recife'
lista[2][1] = 'Porto de Galinhas'
print(lista)

# Concatenando lista com operadores de adição
lista1 = ['do', 're', 'mi']
lista2 = ['fa', 'sol', 'la', 'si']
lista = lista1 + lista2
print(lista)

# Usando funções "max, min e sun" para tratando lista com números
# max(maior) - min(menor) - sum(soma dos elementos)
lista = [15, 23, 12, 5, 9, 2, 11]
print(max(lista))
print(min(lista))
print(sum(lista))

# Inserindo elementos em qualquer posição de uma lista
# Função "append" insere no final de uma lista e "insert" informa qual será a posição realizada
lista = ['do', 'mi', 'fa', 'sol', 'la']
lista.insert(1, 're')
lista.insert(0, 'Luiz')
lista.append('Recife')
print(lista)


# Utilizando função "del" para escluir elementos de uma lista
lista = ['do', 'mi', 'fa', 'sol', 'la']
del lista[2] #fa
print(lista)
del lista[0:3] #Exclui os elementos 0 e 3
print(lista)

# Excluindo ultimo elemento de uma lista por meio da função "pop"
lista = ['do', 'mi', 'fa', 'sol', 'la']
lista.pop() #la
print(lista)
ultimo = lista.pop()
print(ultimo)
primeiro = lista.pop(0)
print(primeiro)

# A função "remove" localiza o elemento e excluir. A função "clear" excluir toda a lista de elementos
lista = ['do', 'mi', 'fa', 'sol', 'la']
lista.insert(1, 're')
lista.insert(7, 'Si')