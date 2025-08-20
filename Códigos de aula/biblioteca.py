# Função sem retorno e sem parâmetro
def ola():
    print("Olá, Bem Vindo!")
    if(True):
        print("Função Válida")
    else:
        print("Erro")

# Função que recebe uma mensagem do tipo str
# e retorna um número inteiro
def inputInt(msg:str):
    
    x = input(f"{msg}")
    
    # O try/except evitam que o programa apresente um erro
    # e para a execução. Ele tenta (try) executar o código
    # e em caso de erro executa a alternativa (except)
    try:
        x = int(x)
    except:
        print("Int inválido!")
        # Funções recursivas fazem uma chamada para ela mesmo
        x = inputInt(f"{msg}")
    return x

# Função sem parâmetro que retorna um valor float
# Enquanto não for possível converter para float, o programa
# continua pedindo um valor ao usuário
def pedirFloat():
    while(True):
        try:
            x = float(input("Numero: "))
            break
        except:
            print("Float inválido")
    return x

# Funções com parâmetros
# Não importa o valor deles, mas sim o comportamento da função
# A função não tem a obrigação de saber os valores, deve apenas calcular o que for necessário
# Podemos especificar o tipo do parâmetro que será recebido
# nomeDoParametro:tipoDele
# Ao separar por vírgula, podemos aumentar a quantidade de parâmetros recebidos
def somar2(x:int, y:int):
    total = x + y
    return total

# Aqui temos três e não importa o tipo deles
def somar3(v1,v2,v3):
    soma = v1 + v2 + v3
    return soma

# Função com dois parâmetros
def pot(valor:int,potencia:int):
    resultado = valor**potencia
    return resultado

# Função com dois parâmetros
def raiz(valor:float,grau:int):
    resultado = valor**(1/grau)
    return resultado

# Cria a função chamada ePar que recebe
# um parametro inteiro e retona:
# True se o parametro for par
# False se o parametro for Impar
def ePar(valor:int):
    resto = valor % 2
    if(resto == 0):
        return True
    else:
        return False

# Crie uma função chamada ehPrimo que recebe
# um número qualquer por parâmetro e returna
# True se o nº for primo ou False se não
"""
Números primos: 1, 2, 3, 5, 7, 11, 13, 
"""
def ehPrimo(x):
    cont = 0
    for i in range(1, x+1):
        if(x % i == 0):
            cont += 1
    
    if(cont == 2):
        return True
    else:
        return False

