import sqlite3
con=sqlite3.connect("meu_banco.db")

try:
    con=sqlite3.connect("meu_banco.db")
    cur=con.cursor()
  #  cur.execute("CREATE TABLE pessoa(id, nome, idade, cpf)")
  #  cur.execute("INSERT INTO pessoa VALUES(1, 'Bruce Wayne', 3, '241.123.354-32')")
    #res=cur.execute("SELECT * FROM pessoa")
    #cur.execute("DELETE FROM pessoa WHERE id=1")
    pessoas=res.fetchone()
    print(pessoas)
    con.commit()
except ConnectionRefusedError as c:
    print('erro de conexão com o banco')