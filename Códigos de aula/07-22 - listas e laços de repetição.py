while (True):
    # Toda vez que começa o programa, cria o vetor vazio
    notas = [0.0] * 7
    # Inicia a variável soma
    soma = 0
    
    # Faz um laço para pedir 7 notas
    for i in range(0,7):
        # Faz o input e armazena no vetor
        notas[i] = float(input(f"nota {i+1}: "))

        # Verifica se é a primeira nota para definir ela como maior e menor
        if(i==0):
            maior = notas[i]
            menor = notas[i]

        # Verifica se a nota atual é a maior
        if(notas[i] > maior):
            maior = notas[i]
        
        # Verifica se a nota atual é a menor
        if(notas[i] < menor):
            menor = notas[i]

        # Faz a soma da nota para depois calcular a média
        soma = soma + notas[i]

    # Remove da soma a maior e a menor nota
    soma = soma - maior - menor
    # Faz a média por 5 porque duas foram removidas
    media = soma/5

    # Apresenta os dados na tela
    print("Notas Descartadas ",menor," e ",maior)
    print("Média: ",media)

    # Verifica se o usuário quer sair do programa
    continuar = input("Continuar?(S/N): ").upper()
    if (continuar == "N"):
        break