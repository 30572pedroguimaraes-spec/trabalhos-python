def CalcularRetangulo(comprimento, largura):
    area = comprimento * largura
    perimetro = 2 * (comprimento + largura)

    return area, perimetro

comprimento = float(input("Introduza o comprimento: "))
largura = float(input("Introduza a largura: "))

area, perimetro = CalcularRetangulo(comprimento, largura)

print("Área:", area)
print("Perímetro:", perimetro)