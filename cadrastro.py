#variavel para cadastro
nome = ""
idade = ""
usuario = ""
senha = ""

#variaveis para login
login_usuario = ""
login_senha = ""

#apenas a tela de visualizacao
while True:
    print("====================")
    print("Sistema de cadrastro")
    print("====================")

    print("1 - cadastrar")
    print("2 - fazer login")
    print("3 - sair")

    opcao= input("Escolher uma opcao: ")
 #funcionalidades
    #se o usuario digitar o valor 1, vai ser exibido
    # a acao abaixo
    if (opcao == "1"):
        print("==============================")
        print("======tela de cadrastro=======")
        print("==============================")
        nome = input ("digite o seu nome: ")
        idade = input ("digita a sua idade: ")
        usuario = input (" digita seu usuario: ")
        senha = input ("coloque sua senha: ")
        print("\n Cadastro realizado!\n")
#se digitar 2, abre a tela de login
    elif (opcao == "2"):
        print("=========================")
        print("======tela de login =====")
        print("=========================")
        login_usuario = input("digite o usuario cadastrado: ")
        login_senha = input("digite a senha : ")

        #processamento de usuario e senha
        if login_usuario == usuario and login_senha == senha :
        print("\n Login realizado com sucesso!\n")
        print("Bem vindo,", nome)
    #se não estiver correto entra no caso abaixo
    else:
        print("Usuario ou senha incorretos")

    #se digitar 3, sai da excução
    elif (opcao == "3"):
        print("vc esta saindo do cadastro,ate mais!")
        break
    #se não for nem 1,2 ou 3, mostrar erro e repetir codigo
    else:
        print("valor digitado,invalidouse apenas numeros inteirosdo menu")
