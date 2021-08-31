# importando SQLite
import sqlite3 as lite

# criando conexão / criando novo BD
con = lite.connect('livraria.db')

# criando tabelas

# Tabela categoria
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE Categoria(id INTEGER, nome TEXT, PRIMARY KEY('id' AUTOINCREMENT) )")


# Tabela Membro
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE Membro(id INTEGER, nome TEXT, genero TEXT, tel TEXT, endereco TEXT, PRIMARY KEY('id' AUTOINCREMENT) )")


# Tabela Livro
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE Livro(id INTEGER, titlo TEXT, actor TEXT, editora TEXT, categoria INTEGER, copias INT, adicionado_em DATE, PRIMARY KEY('id' AUTOINCREMENT), FOREIGN KEY('categoria') REFERENCES 'Categoria' ('id') ON DELETE CASCADE )")


# Tabela Livros_Alugados
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE Livro_Alugado(id INTEGER, id_livro INT, id_membro INT, alugado_em DATE, data_de_retorno DATE, PRIMARY KEY('id' AUTOINCREMENT), FOREIGN KEY('id_livro') REFERENCES 'Livro' ('id') ON DELETE CASCADE, FOREIGN KEY('id_membro') REFERENCES 'Membro' ('id') ON DELETE CASCADE )")
