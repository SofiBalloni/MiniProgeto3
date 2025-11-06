import requests

BASE_URL = "http://127.0.0.1:5000/api/v1/"


def criar_livro():
    print("\n=== CADASTRAR NOVO LIVRO ===")
    titulo = input("Título: ")
    autor = input("Autor: ")
    ano = input("Ano de publicação: ")

    livro = {"titulo": titulo, "autor": autor, "ano": int(ano)}
    response = requests.post(BASE_URL + "livro", json=livro)
    print(response.text)


def listar_livros():
    print("\n=== LISTA DE LIVROS ===")
    response = requests.get(BASE_URL + "livros")
    print(response.text)


def atualizar_livro():
    print("\n=== ATUALIZAR LIVRO ===")
    id_livro = int(input("Digite o ID do livro a ser atualizado: "))
    novo_titulo = input("Novo título: ")
    novo_autor = input("Novo autor: ")
    novo_ano = int(input("Novo ano: "))

    data = {
        "id": id_livro,
        "titulo": novo_titulo,
        "autor": novo_autor,
        "ano": novo_ano
    }

    response = requests.put(BASE_URL + "livro", json=data)
    print(response.text)


def deletar_livro():
    print("\n=== REMOVER LIVRO ===")
    id_livro = int(input("Digite o ID do livro a ser removido: "))
    response = requests.delete(BASE_URL + "livro", json={"id": id_livro})
    print(response.text)


def menu():
    while True:
        print("\n===============================")
        print("       SISTEMA DE LIVROS       ")
        print("===============================")
        print("1 - Cadastrar livro")
        print("2 - Listar livros")
        print("3 - Atualizar livro")
        print("4 - Remover livro")
        print("0 - Sair")
        print("===============================")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criar_livro()
        elif opcao == "2":
            listar_livros()
        elif opcao == "3":
            atualizar_livro()
        elif opcao == "4":
            deletar_livro()
        elif opcao == "0":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()
