soma = 0
while True:
    num = int(input("Digite um número (negativo para sair): "))
    if num < 0:
        break
    soma += num
print(f"Soma dos números positivos: {soma}")