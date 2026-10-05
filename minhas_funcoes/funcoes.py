def ola():
    print("Olá, Mundo!")
    
ola()

def ola(nome):
    print(f"Olá, {nome}!")
nome_digitado = input("\nDigite seu nome: ")

ola(nome_digitado)

def somar():
    num1 = int(input("\nDigite o primeiro numero: "))
    num2 = int(input("Digite o segundo numero: "))
    resultado = num1 + num2
    print(f"\nO resultado de {num1} e {num2} é: {resultado}")

somar()

def cumprimento(nome):
    print(f"\nOlá {nome}!")