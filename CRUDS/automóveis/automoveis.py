import os
import json

arquivo = os.path.join(os.path.dirname(__file__), 'automoveis.json')

if not os.path.exists(arquivo):
    with open(arquivo, 'w') as f:
        json.dump({}, f)

def carregar_automoveis():
    with open(arquivo, 'r') as f:
        return json.load(f)

def salvar_automoveis():
    automoveis = carregar_automoveis()
    with open(arquivo, 'w') as f:
        json.dump(automoveis, f, indent=4)

# CRUD
def adicionar_automovel():
    automoveis = carregar_automoveis()
    marca = input("Digite a marca do automóvel: ")
    categoria = input("Digite a categoria do automóvel: ")
    ano = input("Digite o ano de fabricação do automóvel: ")
    if marca in automoveis:
        print(f"O automóvel {marca} já está cadastrado no sistema.")
    else:
        automoveis[marca] = {'categoria': categoria, 'ano': ano}
        salvar_automoveis()
        print(f"O automóvel {marca} foi adicionado com sucesso!")

def visualizar_automoveis():
    automoveis = carregar_automoveis()
    print("\n Sistema de registros de automóveis: ")
    if automoveis:
        for marca, detalhes in automoveis.items():
            print(f"Marca: {marca} - Categoria: {detalhes['categoria']} - Ano: {detalhes['ano']}")
    else:
        print("Sistema de registros de automóveis vazio.")

def remover_automoveis():
    automoveis = carregar_automoveis()
    marca = input("Insira a marca do automóvel que deseja remover: ")
    if marca in automoveis:
        del automoveis[marca]
        salvar_automoveis()
        print(f"O automóvel {marca} foi removido com sucesso!")
    else:
        print(f"O automóvel {marca} não foi encontrado.")

# Menu
def menu():
    while True:
        print("\n Menu:")
        print("1 - Adicionar Automóvel")
        print("2 - Visualizar Automóveis")
        print("3 - Remover Automóveis")
        print("4 - Sair")

        opcao = input("Insira a opção desejada: ")

        if opcao == "1":
            adicionar_automovel()
        elif opcao == "2":
            visualizar_automoveis()
        elif opcao == "3":
            remover_automoveis()
        elif opcao == "4":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    menu()
