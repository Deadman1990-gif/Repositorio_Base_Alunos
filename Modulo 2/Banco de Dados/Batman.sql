CREATE TABLE IF NOT EXISTS personagem(
    id        INT PRIMARY KEY AUTOINCREMENT,
    nome      VARCHAR(50),
    cor       VARCHAR(30),
    altura    CHAR(4),
    habilidades VARCHAR(40)
    FOREIGN KEY 
);

CREATE TABLE IF NOT EXISTS usuario(
    id             INT PRIMARY KEY AUTOINCREMENT,
    nome_usuário   VARCHAR(25),
    idade          INT,
    FOREIGN KEY id REFERENCES personagem(id)
);

CREATE TABLE IF NOT EXISTS tarefas(
    id              INT PRIMARY KEY AUTOINCREMENT,
    local           MAPA,
    tarefa          VARCHAR(50),
    personagem_nome VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS jogo_livre(
    id              INT PRIMARY KEY AUTOINCREMENT,
    local_mapa      tarefa,
    tempo           CHAR(4)
);

CREATE TABLE IF NOT EXISTS mapa(
    id              INT PRIMARY KEY AUTOINCREMENT,
    locais          VARCHAR(60),
    pontos_tarefa   tarefas,
    missões         jogo livre
);

CREATE TABLE IF NOT EXISTS interface(
    id              INT PRIMARY KEY AUTOINCREMENT,
    jogo            VARCHAR(50),
    personagem      VARCHAR(50)
);