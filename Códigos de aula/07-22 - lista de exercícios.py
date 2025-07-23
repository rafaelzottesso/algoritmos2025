# Crie um vetor e armazene os números de 1 a 100.
# Cada número deve ocupar uma posição do vetor (lista).

# Criação do vetor
numeros = [0] * 100

# Preenchendo o vetor com números de 1 a 100
for i in range(0, len(numeros)):
    numeros[i] = i + 1

# Percorrer o vetor para mostrar os valores dele
print("Números do vetor:")
for i in range(0, len(numeros)):
    print(f"{numeros[i]:3d}", end=" ")

print("") # Esse print finalizar o end do print anterior

# Mostre na tela todos os números do vetor em ordem decrescente (100 a 1).
print("Números da trás para frente:")
for i in range(len(numeros)-1, -1, -1):
    print(f"{numeros[i]:3d}", end=" ")    

print("") # Esse print finalizar o end do print anterior