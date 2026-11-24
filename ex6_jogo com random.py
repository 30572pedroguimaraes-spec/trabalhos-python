
import random

numero_secreto = random.randint(1, 100)

tentativas = 0
numero = 0

print("=== JOGO: ADIVINHA O NÚMERO ===")
print("Tenta descobrir o número entre 1 e 100!")

while numero != numero_secreto:
    numero = int(input("Introduz um número: "))
    tentativas += 1

    if numero < numero_secreto:
        print("O número secreto é MAIOR!")

    elif numero > numero_secreto:
        print("O número secreto é MENOR!")

    else:
        print("\nParabéns! Acertaste no número!")
        print("FIM DE JOGO!")
        print("Número de tentativas:", tentativas)
