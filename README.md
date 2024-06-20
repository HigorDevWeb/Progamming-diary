# Projeto de Banco de Dados SQLite com Python

Este projeto consiste em scripts Python para criar e manipular um banco de dados SQLite. Ele inclui funcionalidades para criar tabelas, adicionar entradas e recuperar dados.

## Estrutura do Projeto

- `app.py`: Arquivo principal do aplicativo.
- `database.py`: Contém funções para interação com o banco de dados SQLite.
- `data.db`: Arquivo do banco de dados SQLite.

## Pré-requisitos

- Python 3.x
- Biblioteca `sqlite3` (já incluída na biblioteca padrão do Python)

## Instruções de Configuração

1. **Clone o repositório ou copie os arquivos para o seu ambiente local**.

2. **Certifique-se de que você tem o Python 3.x instalado**:
   - Você pode baixar o Python em [python.org](https://www.python.org/).

3. **Estrutura do Projeto**:
   - Coloque `app.py`, `database.py` e `data.db` no mesmo diretório.

## Uso

### Inicialização do Banco de Dados

No arquivo `database.py`, temos as seguintes funções:

- `create_table()`: Cria uma tabela chamada `entries` se ela não existir.
- `add_entry(entry_content, entry_date)`: Adiciona uma nova entrada na tabela `entries`.
- `get_entries()`: Recupera todas as entradas da tabela `entries`.

### Exemplo de Uso

Você pode usar as funções do `database.py` no seu aplicativo principal (`app.py`). Aqui está um exemplo de como usá-las:

```python
import database

# Cria a tabela 'entries' se ela não existir
database.create_table()

# Adiciona uma nova entrada
database.add_entry("Minha primeira entrada", "2024-06-20")

# Recupera e imprime todas as entradas
entries = database.get_entries()
for entry in entries:
    print(f"Content: {entry['content']}, Date: {entry['date']}")
