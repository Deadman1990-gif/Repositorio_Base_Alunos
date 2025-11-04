CREATE TABLE IF NOT EXISTS personagem(
    id        INT PRIMARY KEY AUTOINCREMENT,
    nome      VARCHAR(50),
    cor       VARCHAR(30),
    altura    CHAR(4),
    habilidades VARCHAR(40)
);

CREATE TABLE IF NOT EXISTS usuario(
    id             INT PRIMARY KEY AUTOINCREMENT,
    nome_usuario   VARCHAR(25),
    idade          INT,
    idpersonagem   INT,
    FOREIGN KEY (idpersonagem) REFERENCES personagem(id)
);

CREATE TABLE IF NOT EXISTS tarefas(
    id              INT PRIMARY KEY AUTOINCREMENT,
    local_tarefa    VARCHAR(100),
    tarefa          VARCHAR(50),
    idusuario       INT,
    FOREIGN KEY (idusuario) REFERENCES usuario(id)
);

CREATE TABLE IF NOT EXISTS jogo_livre(
    id              INT PRIMARY KEY AUTOINCREMENT,
    tempo           CHAR(4),
    idtarefa        INT,
    FOREIGN KEY (idtarefa) REFERENCES tarefas(id),
);

CREATE TABLE IF NOT EXISTS mapa(
    id              INT PRIMARY KEY AUTOINCREMENT,
    locais          VARCHAR(60),
    pontos_tarefa   CHAR(1000),
    missões         VARCHAR(100)
    FOREIGN KEY (locais) REFERENCES jogo_livre(idjogo_livre)

);

CREATE TABLE IF NOT EXISTS interface(
    id              INT PRIMARY KEY AUTOINCREMENT,
    jogo            VARCHAR(50),
    personagem      VARCHAR(50)
); 

