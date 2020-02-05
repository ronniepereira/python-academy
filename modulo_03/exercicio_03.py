nota_01 = float(input("Digite a primeira nota: "))
nota_02 = float(input("Digite a segunda nota: "))

PESO_NOTA_01 = 3.5
PESO_NOTA_02 = 7.5

nota_final = ((nota_01 * PESO_NOTA_01) +
              (nota_02 * PESO_NOTA_02)) / (PESO_NOTA_01 + PESO_NOTA_02)

print(f"Nota final: {nota_final}")
