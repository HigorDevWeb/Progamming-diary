from database import add_entry, get_entries,create_table
import sqlite3

# Opções do menu exibidas ao usuário
menu = '''Please select one of the following options:
1) Add new entry for today
2) View entries
3) Exit

Your selection: '''
welcome = 'Welcome to the programming diary'

# Função para criar a tabela 'entries' se ela não existir

# Função para solicitar ao usuário a adição de uma nova entrada no diário
def prompt_new_entry():
    entry_content = input("What have you learned today? ")  # Solicita o conteúdo da entrada
    entry_date = input("Enter the date: ")  # Solicita a data
    add_entry(entry_content, entry_date)  # Adiciona a entrada ao banco de dados

# Função para exibir todas as entradas ao usuário
def view_entries(entries):
    for entry in entries:
        print(f"{entry['date']}\n{entry['content']}\n\n")  # Imprime a data e o conteúdo de cada entrada

print(welcome)  # Exibe mensagem de boas-vindas
create_table()
# Loop principal para manter o programa em execução até que o usuário escolha sair
while (user_input := input(menu)) != '3':
    if user_input == '1':
        prompt_new_entry()  # Chama a função para adicionar uma nova entrada
    elif user_input == '2':
        entries = get_entries()  # Recupera todas as entradas do banco de dados
        view_entries(entries)  # Exibe as entradas recuperadas
    else:
        print('Invalid option. Please try again.')  # Lida com seleções de menu inválidas
