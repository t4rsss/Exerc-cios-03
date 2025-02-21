n = int(input("Digite a quantidade de termos da sequência de Fibonacci: "))
a, b = 0, 1
for _ in range(n):
    print(a, end=' ')
    a, b = b, a + b
print()