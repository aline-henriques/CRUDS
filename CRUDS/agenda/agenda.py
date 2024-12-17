import os
import json

arquivo = os.path.join(os.path.dirname(__file__), 'agenda.json')

if not os.path.exists(arquivo):
    with open(arquivo, 'w') as f:
        json.dump({}, f)

def carregar():
    with open(arquivo, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}

def salvar(agenda):
    with open(arquivo, 'w') as f:
        json.dump(agenda, f, indent=4)

def adicionar_contato():
    agenda = carregar()
    nome = input("Insira o nome: ")
    sobrenome = input("Insira o sobrenome: ")
    telefone = input("Insira o telefone: ")
    if nome in agenda:
        print(f"O(a) {nome} já existe na agenda telefônica.")
    else:
        agenda[nome] = {"Sobrenome": sobrenome, "Telefone": telefone}
        salvar(agenda)
        print("Contato salvo com sucesso.")

def remover_contato():
    agenda = carregar()
    nome = input("Insira o nome do contato a ser removido: ")
    if nome in agenda:
        del agenda[nome]
        salvar(agenda)
        print(f"O(a) {nome} foi removido com sucesso.")
    else:
        print(f"O(a) {nome} não existe na agenda telefônica.")

def visualizar_contatos():
    agenda = carregar()
    if agenda:
        print("\nAgenda Telefônica:")
        for nome, detalhes in agenda.items():
            print(f"Nome: {nome}, Sobrenome: {detalhes['sobrenome']}, Telefone: {detalhes['telefone']}")
    else:
        print("\nAgenda vazia.")

def menu():
    while True:
        print("\n1 - Adicionar Contato")
        print("2 - Remover Contato")
        print("3 - Visualizar Contatos")
        print("4 - Sair")

        opcao = input("Insira a opção desejada: ")

        if opcao == '1':
            adicionar_contato()
        elif opcao == '2':
            remover_contato()
        elif opcao == '3':
            visualizar_contatos()
        elif opcao == '4':
            print("Saindo da agenda!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    menu()
