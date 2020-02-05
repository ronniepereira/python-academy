numero_01 = int(input("Digite o primeiro numero inteiro: "))
numero_02 = int(input("Digite o segundo numero inteiro: "))
numero_03 = float(input("Agora.. Digite a primeiro numero real: "))

resultado_01 = (numero_01 * 2) * (numero_02 / 2)
resultado_02 = (numero_01 * 3) + numero_03
resultado_03 = numero_03**3
print(
    f"Resultado do produto do dobro do primeiro numero e metade do segundo numero: {resultado_01}"
)

print(
    f"Resultado do triplo do primeiro numero mais terceiro numero: {resultado_02}"
)

print(f"Resultado terceiro numero elevado ao cubo: {resultado_03}")
