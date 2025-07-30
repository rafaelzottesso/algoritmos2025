# Biblioteca pra rodar comandos no terminal
import os

# Enquanto o tamanho do nome do email for menor que 6, o usuário deverá informar novamente
tamanho = 0
while(tamanho < 6):
    usuario = input("Informe seu usuário de email: ")
    tamanho = len(usuario)
    if(tamanho <= 5):
        print("Informe um email maior que 5 caracteres.")

# Apresenta o nome do email
print(f"\nSeu nome de usuário: {usuario}")

print("\nDefina seu provedor de emails...")
print("1 - @ifpr.edu.br")
print("2 - @gmail.com")
print("3 - @hotmail.com")
print("4 - outro")
opcao = int(input("OPÇÃO: "))

# Verifica a opção do usuário para completar o usuário de email com o provedor
if(opcao == 1):
    email = usuario + "@ifpr.edu.br"
elif(opcao == 2):
    email = usuario + "@gmail.com"
elif(opcao == 3):
    email = usuario + "@hotmail.com"
else:
    # Se o provedor não tiver "@" E não tiver ".com", informe novamente
    provedor = ""
    while(not("@" in provedor) and not(".com" in provedor)):
        provedor = input("Digite seu provedor de email com @: ")

    email = usuario + provedor

print(f"Seu email é: {email}")

# Verifica com o usuário se o email está correto
correto = input("Seu email está correto? (S) Sim ou (N) Não: ")
if(correto != "S" and correto != "s"):
    exit() # Finaliza o programa

msg_commit = input("\nMensagem do commit: ")
while( len(msg_commit) <= 10 ):
    print("Detalhe mais sua mensagem!")
    msg_commit = input("Mensagem do commit: ")

print("------------------------------")
print("Iniciando processos do Git...")
print("------------------------------")

# Executar os comandos do git no terminal
    
# Configurar o email
c = f"git config user.email \"{email}\"  "
os.system(c)

# Identificar as novidades e incluir no commit
c = f"git add *"
os.system(c)

# Registrar o commit com uma mensagem
c = f"git commit -m \"{msg_commit}\"  "
os.system(c)

# Enviar para os servidores do GitHub
c = "git push"
os.system(c)