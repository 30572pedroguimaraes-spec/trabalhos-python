def CalcularResultados(num1, num2):
    soma = num1 + num2
    produto = num1 * num2
    return soma, produto


# Programa principal
num1 = int(input("Introduza o primeiro número: "))
num2 = int(input("Introduza o segundo número: "))

soma, produto = CalcularResultados(num1, num2)

print("\nSoma:", soma)
print("Produto:", produto)