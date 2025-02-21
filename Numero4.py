a = int(input("Digite o primeiro número do intervalo: "))
b = int(input("Digite o segundo número do intervalo: "))
for i in range(min(a, b), max(a, b) + 1):
    if i % 2 != 0:
        print(i)