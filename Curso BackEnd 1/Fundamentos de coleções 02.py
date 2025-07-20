'''
LISTA: Na linguagem Python, listas são estruturas de dados compostas por elementos de
diversos tipos, organizados linearmente, como uma espécie de vetor.
Cada elemento de uma lista é identificado por um índice ou subscrito, que
começa na posição 0 (zero) e termina na quantidade de elementos menos um
(n - 1) (MATTHES, 2016).
'''

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
print(lista)
lista.remove('do')
print(lista)
lista.clear()
print(lista)

# As funções "sort""reverse" ordenam e invertem valores.
# A função "len" informa tamanho da lista
lista = [15,23,12,5,9,2,11]
lista.sort()
print(lista)
lista.reverse()
print(lista)
print(len(lista))

# Estrutura de repetição "for" percorrendo lista
lista = ['do', 're', 'mi', 'fa', 'sol', 'la'] #lista
tamanho = len(lista)  # Mostra o tamanho da lista

for indice in range(0,tamanho): # Opção 1 para percorrer a lista
    print(lista[indice])

for elemento in lista: # Opção 2 para percorrer a lista
    print(elemento)

'''
TUPLAS: Assim como uma lista, a tupla é uma estrutura de dados heterogênea que
pode ser composta por objetos de diversos tipos, como str, int, float e
outros. Apesar de possuírem algumas similaridades, existem diversas diferenças entre listas e tuplas,
sendo a principal delas o fato de que as tuplas são imutáveis — ou seja, 
não é possível incluir, excluir ou alterar seus elementos
(MUELLER, 2019).
'''

tupla1 = tuple("aeiou")
tupla2 = "a", "e", "i", "o", "u"
tupla3 = ("a","e","i","o","u")
print(tupla1)
print(tupla2)
print(tupla3)

tupla = ()
print(tupla)


# Uma tupla de apenas um elemento precisa ter uma virgula para que seja identificada como tupla e não
# uma declaração de um tipo

tupla = (1,)
inteiro = (1)
print(tupla)
print(inteiro)

tupla = (1.0,)
real = (1.0)
print(tupla)
print(real)

tupla = ("1",)
texto = ("1")
print(tupla)
print(texto)

# Acessar um elemento de uma tupla é igual a lista, utilizando "indice"
# O primeiro elemento é o [0] e o ultimo é o [-1]
tupla = "a", "e", "i", "o", "u"
print(tupla[0])
print(tupla[-1])
print(tupla[0:2])

# Uma tupla pode conter uma lista e neste caso, os elementos podem ser alterados

tupla = 1, 2, 3,['a', 'b', 'c']
print(tupla)
tupla[3][1] = 'z'
print(tupla)

# Como nos exemplos acima, uma tupla não pode ser modificada, porém, pode ser concatenada.
# Essa operação na verdade cria outra tupla com o mesmo nome
tupla = "domingo", "segunda", "terça"
tupla += "quarta", "quinta", "sexta", "sabado"
print(tupla)

# A tupla também pode ser percorrida utilizando o "for", acessando os elementos
tupla = "domingo", "segunda", "terça", "quarta", "quinta", "sexta", "sabado"
tamanho = len(tupla)

for indice in range(0, tamanho):    #Usando o "range" para percorrer os elementos
    print(tupla[indice])

for elemento in tupla:    # Usando o in para percorrer os elementos
    print(elemento)

'''
Em Python, um dicionário (array associativo) é uma estrutura de objetos
representados por pares que contêm chave e valor, na qual a chave é utilizada
como índice para localizar determinado valor. A chave pode ser um elemento
de qualquer tipo, não necessariamente um número
Para criar um dicionário manualmente, insira elementos por meio de uma
estrutura envolvida por chaves

  ________________________
 |   CHAVE       VALOR    |
  ------------------------
     123         Elena
     125         Luiz
     222         Gustavo
'''

# É possivel criar um dicionario com uma lista de elementos usando a instrução "Dict".
# A lista deve estar composta por pares de tupla
lista = [('123', 'Elena'), ('125', 'Luiz'), ('222', 'Gustavo')]
dicionario = dict(lista)
print(dicionario)

print(dicionario['123'])
print(dicionario['125'])
print(dicionario['222'])

# Outra forma de localizar um valor no dicionario é usando funçao "get"
nome1 = dicionario.get('123')
print(nome1)
nome2 = dicionario.get('222')
print(nome2)
nome3 = dicionario.get('125')
print(nome3)

# Para alterar o valor de uma chave no dicionario é dessa forma
dicionario['123'] = 'Mariana'
print(dicionario)
dicionario['222'] = 'Elena'
print(dicionario)

# Poder incluir uma nova entrada ao dicionario informando a chave e o valor, mas também
# Pode ser usado o metodo "update"
dicionario['142'] = 'Pedrosa'
print(dicionario)
dicionario.update({'109':'Sestito', '144':'Sara'})
print(dicionario)

#Para remover um elemento do dicionario é através da chave ou pela funcao "pop".
# Essa função permite retornar uma mensagem
del dicionario['123'] #Remoção da chave 123 e do seu valor
print(dicionario)

nome = dicionario.pop('123', 'não encontrado para excluir') # Se o numero existir ele apaga.
print(nome)                                                 # Se não existir ele mostra a mensagem

nome = dicionario.pop('222', 'Não encontrado para excluir') # Aqui ele apaga a chave e não mostra a frase
print(nome)
nome = dicionario.pop('222', 'Gustavo ja foi apagado')  # Aqui a chave já não existe, então ele mostra a frase
print(nome)

#  É possivel percorrer o dicionario utilizando a estrutura "for"
for chave in dicionario:
    print(chave, dicionario[chave])

# As funções "Keys" "values" e "items" retornam as chaves respectivas, os valores e as tuplas de cada elemento do dicionario
print(dicionario.keys()) # Retornara assim: dict_keys(['125', '142', '109', '144'])
print(dicionario.values()) # Retornara assim: dict_values(['Luiz', 'Pedrosa', 'Sestito', 'Sara'])
print(dicionario.items()) # Retornara assim: dict_items([('125', 'Luiz'), ('142', 'Pedrosa'), ('109', 'Sestito'), ('144', 'Sara')])

