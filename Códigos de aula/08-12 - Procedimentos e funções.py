import biblioteca as bib
#bib.ola()

num1 = bib.inputInt("Digite um número: ")
num2 = bib.inputInt("Digite outro: ")
print("os números são: ",num1," ",num2)

res = bib.somar2(num1, num2)
print(f"{num1} + {num2} = {res}")

raiz = bib.raiz(num1, num2)
print(f"A raiz de {num1} com grau {num2} é {raiz}")

res = bib.pot(num1, num2)
print(f"{num1} elevado a {num2} é {res}")

num3 = bib.inputInt("Mais um int: ")
res = bib.somar3(num1, num2, num3)
print("A soma dos números é", res)

tipo = bib.ePar(num1)
if(tipo == True):
    print(f"{num1} é par")
else:
    print(f"{num1} é ímpar")

# Mostrar na tela todos os números primos
# do 1 ao 100
    