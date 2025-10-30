import sqlite3
con=sqlite3.connect("Jogo_Do_Batman.db")

try:
    con=sqlite3.connect("Jogo_Do_Batman.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE jogo(skin, personagens, tempo)")
    cur.execute("CREATE TABLE usuário(id, nome, idade)")
    cur.execute("CREATE TABLE personagem(nome, id, cor, altura, habilidades)")
    cur.execute("CREATE TABLE missões(local, tarefa, personagem)")
    cur.execute("CREATE TABLE jogo livre(local, tempo, personagens)")
    cur.execute("CREATE TABLE mapa(id, nome do personagem, nome da area, ponto de tarefa)")
    cur.execute("CREATE TABLE interface(jogo=Batman, personagem)")
    cur.execute("INSERT INTO ")