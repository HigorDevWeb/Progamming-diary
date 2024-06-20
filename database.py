import sqlite3  # Importa o módulo sqlite3 para trabalhar com bancos de dados SQLite

# Conecta ao banco de dados chamado 'data.db'. Se o banco de dados não existir, ele será criado.
conection = sqlite3.connect('data.db')

# Define o método de fábrica de linha para sqlite3.Row, que permite acessar os resultados por nome de coluna.
conection.row_factory = sqlite3.Row

def create_table():
    # Cria uma tabela chamada 'entries' se ela não existir.
    # A tabela tem duas colunas: 'content' para o conteúdo da entrada e 'date' para a data da entrada.
    with conection:
        conection.execute("CREATE TABLE IF NOT EXISTS entries(content TEXT, date TEXT);")
        
def add_entry(entry_content, entry_date):
    # Adiciona uma nova entrada na tabela 'entries' com o conteúdo e a data fornecidos.
    with conection:
        conection.execute(
            "INSERT INTO entries VALUES(?,?);", (entry_content, entry_date)
        )

def get_entries():
    # Seleciona todas as entradas da tabela 'entries'.
    cursor = conection.execute("SELECT * FROM entries")
    return cursor
