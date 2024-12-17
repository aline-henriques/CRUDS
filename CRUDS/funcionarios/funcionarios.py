import os
import json

arquivo = os.path.join(os.path.dirname(__file__), 'funcionarios.json')

if not os.path.exists(arquivo):
    with open(arquivo, 'w') as f:
        json.dump({}, f)

def carregar():
    with open(arquivo, 'r') as f:
        return json.load(f)

def salvar(funcionarios):
    with open(arquivo, 'w') as f:
        json.dump(funcionarios, f, indent=4)

def adicionar_funcionario():
    funcionarios = carregar()
    nome = input("Insira o nome do funcionário: ")
    cargo = input("Insira o cargo do funcionário: ")
    salario = input("Insira o salário do funcionário: ")
    if nome in funcionarios:
        print(f"O funcionário {nome} já está cadastrado no sistema.")
    else:
        funcionarios[nome] = {'cargo': cargo, 'salario': salario}  # Corrigido de 'funcionario' para 'funcionarios'
        salvar(funcionarios)
        print(f"O funcionário {nome} foi adicionado com sucesso!")

def visualizar_funcionarios():  
    funcionarios = carregar()
    print("\n Cadastro de Funcionários atual: ")
    if funcionarios:
        for nome, detalhes in funcionarios.items():
            print(f"Funcionário: {nome} - Cargo: {detalhes['cargo']}, Salário: {detalhes['salario']}")  # Corrigido 'Cargo' e 'Salário' para 'cargo' e 'salario'
    else:
        print("Sistema de cadastro de funcionários vazio.")

def remover_funcionario():
    funcionarios = carregar()
    nome = input("Digite o nome do funcionário que você deseja remover: ")
    if nome in funcionarios:
        del funcionarios[nome] 
        salvar(funcionarios)
        print(f"O funcionário {nome} foi removido do sistema com sucesso.")
    else:
        print(f"O funcionário {nome} não foi encontrado no sistema.")

def menu():
    while True:
        print("\n Menu: ")
        print("1 - Adicionar funcionário")
        print("2 - Visualizar funcionários")
        print("3 - Remover funcionário")
        print("4 - Sair.")
       
        opcao = input("Insira a opção desejada: ")
      
        if opcao == '1':
            adicionar_funcionario()
        elif opcao == '2':
            visualizar_funcionarios()
        elif opcao == '3':
            remover_funcionario()
        elif opcao == '4':
            print("Saindo do sistema.")
            break 
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    menu()