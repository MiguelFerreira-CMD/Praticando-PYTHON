contador = 10
while contador >= 1:
    print(f"Contagem atual: {contador}")
    contador = contador - 1

senha = "1"
tentativa = ""
while senha != tentativa:
    tentativa = input("\nDigite sua senha: ")
    if tentativa == senha:
        print("Acesso liberado!\n")
    else:
        print(("\nSenha incorreta! Tente novamente."))

compras = ["Arroz", "Feijão", "Leite", "Pão"]
for item in compras:
    print(f"Voce precisa comprar: {item}")

print("\n")

numeros = [5, 4, 2, 3, 8, 6, 9, 1, 11]
for numero in numeros:
    if numero % 2 == 0:
        break
    print(numero)

print("\n")

numeros = [5, 4, 2, 3, 8, 6, 9, 1, 11]
for numero in numeros:
    if numero % 2 == 0:
        continue
    print(numero)