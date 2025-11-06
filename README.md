# Mini Projeto – Consumo de API (Biblioteca de Livros)

Este projeto foi desenvolvido como atividade prática da disciplina de **Linguagem de Programação II**.  
O objetivo é criar uma API com **Flask** e um cliente que consome essa API com **Requests**, simulando o funcionamento de um sistema de **biblioteca de livros**.

---

## 🧩 Estrutura do Projeto

```
meu_projeto_api/
│
├── README.md
├── requirements.txt
│
├── server/
│   └── app/
│       └── main.py
│       └── __init__.py
│       └── .env.example
│
└── client/
    └── main.py
    └──.env.example
```

---

## 🚀 Como Executar

### 1. Instalar dependências
```bash
python -m pip install -r requirements.txt
```

### 2. Executar o servidor
```bash
python server/app/main.py
```

### 3. Executar o cliente
```bash
python client/main.py
```

---

## 📚 Exemplo de Uso

**Cadastrar livro**
```
Título: Dom Casmurro
Autor: Machado de Assis
Ano: 1899
```

**Listar livros**
```
ID: 1
Título: Dom Casmurro
Autor: Machado de Assis
Ano: 1899
```

**Atualizar livro**
```
Digite o ID: 1
Novo título: Dom Casmurro (Edição Especial)
Novo autor: Machado de Assis
Novo ano: 1900
```

**Remover livro**
```
Digite o ID: 1
Livro removido com sucesso!
```

---

## 🧠 Endpoints da API

| Método | Rota              | Descrição                | Exemplo de Uso |
|--------|-------------------|--------------------------|----------------|
| GET    | `/api/v1/livros`  | Lista todos os livros    | `/api/v1/livros` |
| POST   | `/api/v1/livro`   | Cadastra um novo livro   | `{"titulo":"1984","autor":"George Orwell","ano":1949}` |
| PUT    | `/api/v1/livro`   | Atualiza um livro        | `{"id":1,"titulo":"1984","autor":"Orwell","ano":1950}` |
| DELETE | `/api/v1/livro`   | Remove um livro          | `{"id":1}` |

---

## 🧰 Tecnologias Utilizadas
- **Python 3**
- **Flask**
- **Requests**
- **JSON**

Ana Beatriz Alves
Sofia Balloni

---
