num = int(input("Número: "))

x = int(input("Valor inicial: "))
y = int(input("Valor final: "))

for i in range(x, y+1):
    print(f"{num} X {i} = {num*i}")
