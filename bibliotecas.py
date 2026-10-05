import time
import random

print("Aguarde...")
time.sleep(2)

print("\nFinalizado!")

print("\n")

while True:
    numero_aleatorio = random.randint(1, 50)
    print(numero_aleatorio)

    time.sleep(1)

    if numero_aleatorio % 2 == 0:
        break