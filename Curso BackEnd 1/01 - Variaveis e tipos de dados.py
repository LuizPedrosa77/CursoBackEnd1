'''
int: conjunto dos numeros inteiros
float: numeros decimais
bool: verdadeiro ou falso
str: textos (string)
complex: numeros complexos (reais e imaginarios
'''

'''
# (input) serve para escrever na tela
nome = input('Digite seu nome: ')
print(nome)

# para usar (input) para ler numero é preciso converter
num_int = int(input("Digite seu dia de nascimento: "))
print(num_int)
'''

# interpolar variavel em outra variavel do tipo str(string)
'''
nome = input('Digite seu nome: ')
frase1 = "Olá, {}. Seja bem-vindo!".format(nome)
frase2 = f'Olá, {nome}. Seja bem-vindo!'

print(frase1)
print(frase2)
'''

# Conversão de tipos de dados
'''
texto = str(65)
texto += str(35.8)
print(texto) #Saída: 6535.8

n1 = int("34")
n2 = float("34.5")
print(n1, ', ', n2) #Saída: 34 , 34.5
'''

# Escopo de variáveis global e local com chamada de função
'''
numero_geral = 15
def imprime_local():
    numero = 10
    print(numero)
imprime_local()
print(numero_geral)
'''

# Exemplo prático de variáveis global e local
'''
# LINHAS INICIAIS:
cliente = "João"
passo = 0
status = "Aguardando novo pedido"


# FUNÇÃO atender()
def atender():
    global passo
    passo += 1
    status = "Pedido recebido."
    print(f"Passo {passo}: {status}")
    preparar()


# FUNÇÃO preparar()
def preparar():
    global passo
    passo += 1
    status = "preparando..."
    print(f"Passo {passo}: {status}")
    entregar


# FUNÇÃO entregar()
def entregar():
    global passo
    passo += 1
    status = "Pedido entregue"
    print(f"Passo {passo}: {status} ao {cliente}!")

atender()
print(status)
'''

# EXERCÍCIO

num1 = 0.0
num2 = 0.0
num3 = 0.0

def ler_numeros():
    global num1, num2, num3
    num1 = float(input("Digite o primeiro numero: "))
    num2 = float(input("Digite o segundo numero: "))
    num3 = float(input("Digite o terceiro numero: "))
    print(f"Os números lidos são: {1}, {2} e {3}.")

def calcular_somar():
    soma = num1 + num2 + num3
    print(f"A soma é: {soma}.")

def calcular_media():
    media = (num1 + num2 + num3) / 3
    print(f"A média é: {media}.")

ler_numeros()
calcular_somar()
calcular_media()