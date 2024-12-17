import os
import json

arquivo = os.path.join(os.path.dirname(__file__), 'livros.json')

if not os.path.exists(arquivo):
    with open(arquivo, 'w') as f:
        json.dump({}, f)

def carregar():
    with open(arquivo, 'r') as f:
        return json.load(f)

def salvar(livros):
    with open(arquivo, 'w') as f:
        json.dump(livros, f, indent=4)
    print("Livro salvo com sucesso!")

def adicionar_livro():
    livros = carregar()
    titulo = input("Insira o título do livro: ")
    autor = input("Insira o nome do autor: ")
    ano = input("Insira o ano de lançamento do livro: ")
    if titulo in livros:
        print(f"O livro {titulo} já está cadastrado no sistema.")
    else:
        livros[titulo] = {'autor': autor, 'ano': ano}
        salvar(livros)
        print(f"O livro {titulo} foi adicionado com sucesso!")

def visualizar_livros():
    livros = carregar()
    print("\n Biblioteca de livros: ")
    if livros:
        for titulo, detalhes in livros.items():
            print(f"Título: {titulo} - Autor: {detalhes['autor']}, Ano: {detalhes['ano']}")
    else:
        print("Biblioteca vazia.")

def remover_livro():
    livros = carregar()
    titulo = input("Digite o título do livro que deseja remover: ")
    if titulo in livros:
        del livros[titulo]
        salvar(livros)
        print(f"O livro {titulo} foi removido com sucesso!")
    else:
        print(f"O livro {titulo} não foi encontrado na biblioteca.")

def menu():
    while True:
        print("\n Biblioteca de Livros: ")
        print("1 - Adicionar Livro")
        print("2 - Visualizar Livros")
        print("3 - Remover Livro")
        print("4 - Sair.")

        opcao = input("Escolha uma opção: ")
         
        if opcao == '1':
            adicionar_livro()
        elif opcao == '2':
            visualizar_livros()
        elif opcao == '3':
            remover_livro()
        elif opcao == '4':
            print("Saindo da biblioteca.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    menu()