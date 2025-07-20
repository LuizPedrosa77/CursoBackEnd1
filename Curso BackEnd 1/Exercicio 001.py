num1 = 1.024
num2 = 2

divisao = num1 / num2
print("Resultado:", divisao)
print("Eu estudo Python")


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
