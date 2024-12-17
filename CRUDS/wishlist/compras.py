import os
import json

arquivo = os.path.join(os.path.dirname(__file__), 'compras.json')

if not os.path.exists(arquivo):
    with open(arquivo, 'w') as f:
        json.dump({}, f)

def carregar():
    with open(arquivo, 'r') as f:
        return json.load(f)

def salvar(itens):
    with open(arquivo, 'w') as f:
        json.dump(itens, f, indent=4)
    print("Salvo com sucesso!")

def adicionar_item():
    itens = carregar()
    nome = input("Insira o nome do item desejado: ").strip()
    quantidade = input("Insira a quantidade: ").strip()
    valor = input("Insira o valor: ").strip()
    if nome in itens:
        print(f"O item '{nome}' já existe na sua lista de desejos.")
    else:
        itens[nome] = {'Quantidade': quantidade, 'Valor': valor}
        salvar(itens)
        print(f"O item '{nome}' foi adicionado à sua lista de desejos com sucesso!")

def remover_item():
    itens = carregar()
    nome = input("Insira o nome do item que você deseja remover: ").strip()
    if nome in itens:
        del itens[nome]
        salvar(itens)
        print(f"O item '{nome}' foi removido da lista de desejos.")
    else:
        print(f"O item '{nome}' não foi encontrado na lista de desejos.")

def visualizar_itens():
    itens = carregar()
    print("\nWishlist:")
    if itens:
        for nome, detalhes in itens.items():
            print(f"{nome}: Quantidade - {detalhes['Quantidade']}, Valor - {detalhes['Valor']}")
    else:
        print("Sua wishlist está vazia.")

def menu():
    while True:
        print("\nMenu:")
        print("1 - Adicionar Item")
        print("2 - Remover Item")
        print("3 - Visualizar Itens")
        print("4 - Sair.")

        opcao = input("Digite a opção desejada: ").strip()

        if opcao == '1':
            adicionar_item()
        elif opcao == '2':
            remover_item()
        elif opcao == '3':
            visualizar_itens()
        elif opcao == '4':
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    menu()
