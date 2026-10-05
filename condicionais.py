idade = int(input("Qual e a sua idade? "))
if idade >= 18 and idade <= 100:
    print("Está liberado!")
elif idade <= 17  and idade >= 1:
    print("Não está  liberado!")
else:
    print("Dados Inválidos!")

senha = "12345"
tentativa = input("\nDigite sua senha: ")
if senha == tentativa:
    print("Acesso liberado!")
else:
    print("Acesso negado!")

