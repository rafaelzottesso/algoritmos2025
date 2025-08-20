import biblioteca as bib

#Criar um vetor e armazenar 5 números
#inteiros digitados pelo usuário.
#Em seguda, percorra o vetor e identifique
#se cada número é primo ou não.

numeros = [0] * 5 # Criar o vetor de 5 num
for i in range(0, len(numeros)): # Percorrer o vetor
    numeros[i] = bib.inputInt(f"Número {i+1}: ") # Digitar um valor inteiro e armazenar

for i in range(0, len(numeros)): # Percorrer o vetor    
    primo = bib.ehPrimo(numeros[i]) # Armazena o retorno da função
    if(primo): # Se for True, mostra a mensagem
        print(f"{numeros[i]} é primo!")
    else: # Se não, mostra outra
        print(f"{numeros[i]} não é primo!")


"""
# Verificar quais números entre 1 e 100 são primos
for v in range(1, 101):
    resposta = bib.ehPrimo(v) 

    if(resposta):
        print(v, "é primo")

# Verificar se um número informado pelo usuário é primo        
x = int(input("Informe número: "))
resposta = bib.ehPrimo(x) 

if(resposta):
    print("é primo")
else:
    print("não é primo")
"""