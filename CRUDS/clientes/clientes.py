import os
import json

arquivo = os.path.join(os.path.dirname(__file__), 'clientes.json')

if not os.path.exists(arquivo):
    with open(arquivo, 'w') as f:
        json.dump({}, f)

def carregar_clientes():
    with open(arquivo, 'r') as f:
        return json.load(f)

def salvar_clientes(clientes):
    with open(arquivo, 'w') as f:
        json.dump(clientes, f, indent=4)
        print("Dados salvos com sucesso!")

def adicionar_cliente():
    clientes = carregar_clientes()
    nome = input("Insira o nome do cliente: ")
    email = input("Insira o e-mail do cliente: ")
    telefone = input("Insira o telefone do cliente: ")
    if nome in clientes:
        print(f"O(a) cliente {nome} já está cadastrado no sistema.")
    else:
        clientes[nome] = {'e-mail': email, 'telefone': telefone}
        salvar_clientes(clientes)
        print(f"O(a) cliente {nome} foi cadastrado com sucesso!")

def visualizar_clientes():
    clientes = carregar_clientes()
    print("\nSistema de clientes atual:")
    if clientes:
        for nome, detalhes in clientes.items():
            print(f"Nome: {nome}, E-mail: {detalhes['e-mail']}, Telefone: {detalhes['telefone']}")
    else:
        print("Nenhum cliente cadastrado no sistema.")

def atualizar_cliente():
    clientes = carregar_clientes()
    nome = input("Insira o nome do cliente que deseja atualizar: ")
    if nome in clientes:
        email = input("Insira o novo e-mail do cliente: ")
        telefone = input("Insira o novo telefone do cliente: ")
        clientes[nome] = {'e-mail': email, 'telefone': telefone}
        salvar_clientes(clientes)
        print(f"Os dados do(a) cliente {nome} foram atualizados com sucesso!")
    else:
        print(f"O(a) cliente {nome} não foi encontrado.")

def remover_cliente():
    clientes = carregar_clientes()
    nome = input("Insira o nome do cliente que deseja remover: ")
    if nome in clientes:
        del clientes[nome]
        salvar_clientes(clientes)
        print(f"O(a) cliente {nome} foi removido com sucesso!")
    else:
        print(f"O(a) cliente {nome} não foi encontrado.")

def menu():
    while True:
        print("\n Menu: ")
        print("1 - Adicionar cliente")
        print("2 - Visualizar clientes")
        print("3 - Atualizar cliente")
        print("4 - Remover cliente")
        print("5 - Sair")

        opcao = input("Escolha a opção desejada: ")
        if opcao == "1":
            adicionar_cliente()
        elif opcao == "2":
            visualizar_clientes()
        elif opcao == "3":
            atualizar_cliente()
        elif opcao == "4":
            remover_cliente()
        elif opcao == "5":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    menu()
