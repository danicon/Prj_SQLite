# importando SQLite
import sqlite3 as lite

# criando conexão / criando novo BD
con = lite.connect('livraria.db')
'''
# inserindo dados
with con:
    cur = con.cursor()
    cur.execute("INSERT INTO Categoria (nome) VALUES ('Romance') ")
    cur.execute("INSERT INTO Categoria (nome) VALUES ('Drama') ")
    cur.execute("INSERT INTO Categoria (nome) VALUES ('Aventura') ")
    cur.execute("INSERT INTO Categoria (nome) VALUES ('Terror') ")
    cur.execute("INSERT INTO Categoria (nome) VALUES ('Comedia') ")

'''


# inserindo update
valores = [1]
with con:
    cur = con.cursor()
    query = "DELETE FROM Livro WHERE id=?"
    cur.execute(query, valores)




cur = con.cursor()
cur.execute("SELECT * FROM Livro")
print(cur.fetchall())