import sqlite3
con=sqlite3.connect("meu_banco.db")

try:
    con=sqlite3.connect("meu_banco.db")
    cur=con.cursor()
    #cur.execute("CREATE TABLE pessoa(id, nome, idade, cpf)")
    # cur.execute("INSERT INTO pessoa VALUES(1, 'Bruce Wayne', 3, '241.123.354-32')
    cur.execute("INSERT INTO pessoa VALUES  (2, 'Thomas Wayne', 45, '241.123.354-32')")
    cur.execute("INSERT INTO pessoa VALUES(3, 'Martha Wayne', 30, '321.324.456-54')")
    cur.execute("INSERT INTO pessoa VALUES(4, 'Alfred Pennyowrth', 38, ' 809.786.654-76')")
    cur.execute("INSERT INTO pessoa VALUES  (5, 'Selina Kyle', 20, '41.13.354-3')")
    cur.execute("INSERT INTO pessoa VALUES  (6, 'Jason Todd', 17, '41.13.354-3')")
    cur.execute("INSERT INTO pessoa VALUES  (7, 'Tim Drake', 17, '41.13.354-3')")
    cur.execute("INSERT INTO pessoa VALUES  (8, 'Dick Grayson', 21, '41.13.354-3')")
    cur.execute("INSERT INTO pessoa VALUES  (9, 'Damian Wayne', 15, '41.13.354-3')")
    cur.execute("INSERT INTO pessoa VALUES  (10, 'Barbara Gordon', 15, '41.123.354-32')")
    
    res=cur.execute("SELECT * FROM pessoa")
    #cur.execute("DELETE FROM pessoa WHERE Nome='Selina Kyle'")
    pessoas=res.fetchall()
    print(pessoas)
    con.commit()
except ConnectionRefusedError as c:
    print('erro de conexão com o banco')