filmes={
    "drama": ["Ainda Estou Aqui","O Poderoso Chefão", "Ela", "A Culpa é Das Estrelas", "A Ultima Música"],
    "comédia": ["Tempos Modernos","American Pie","Dr. Dolittle", "A morte de Stalin", "Heróis fora de Órbita"],
    "policial": ["O Exterminador do Futuro","O Procurado","Velozes e Furiosos", "The Town", "Stolen"],
    "guerra": ["Rambo","1917","Até o Último Homem", "Pecados de Guerra","A Queda"],
    "Ação":["Batman o cavaleiro das trevas", "batman", "Batman e Robin", "Batman vs Duas Caras", "Batman Begins"],
    "Terror":["Terrifier", "Terrifier 2", "Terrifier O Inicio", "Terrifier 3", "Ursinho pooh, sangue e mel"],
    "Shows":["Kiss Rocks vegas", "AC/DC Live At River Plate", "Black Sabbath(2014)", "Kiss 2020 Goodbye live Dubai", "Iron Maiden Live Rock In Rio 2019"],
    "Luta Livre":["WWE", "SmackDown", "Raw", "Survivor Series", "Wreslemania", "SummerSlam"],
    "Trapalhadas, Infantil":["Tom E Jerry", "Scooby-doo", "Looney Tunes", "A Pantera Cor De Rosa", "Os Simpsons"]
}
página=open("filmes.html","w", encoding="utf-8")
página.write("""
<!DOCTYPE html>
    <html lang="pt-BR">
        <head>
        <meta charset="utf-8">
        <title>Filmes</title>
        </head>
        <body> 
""")
for c, v in filmes.items():
    página.write("<h1>%s</h1>" % c)
    for e in v:
        página.write("<h2>%s</h2>" % e)
página.write("""
</body>
</html>
""")
página.close()