CREATE TABLE IF NOT EXISTS livro (
    idlivro             INTEGER PRIMARY KEY AUTOINCREMENT,
    genero              VARCHAR(50),
    titulo              VARCHAR(50),
    dataPublicaçao      DATE,
    autor               VARCHAR(200),
);

CREATE TABLE IF NOT EXISTS aluno (
    idAluno             INTEGER PRIMARY KEY AUTOINCREMENT,
    nome                VARCHAR(255),
    celular             VARCHAR(15),
    turma               CHAR(1)
);

CREATE TABLE IF NOT EXISTS emprestimo(
    idEmprestimo        INTEGER PRIMARY KEY AUTOINCREMENT,
    VALOR               REAL,
    idlivro             INTEGER, 
    FOREIGN KEY         (idAluno)   REFERENCES aluno(idAluno),
    FOREIGN KEY         (idlivro)   REFERENCES livro(idlivro),
);

INSERT INTO aluno(nome, celular, turma)
VALUES
('Pedro Henrique', '3214325434', '1'),
('Thiago', '3214325434', '1'),
('Arthur', '3214325434', '1'),
('Leandro', '3214325434', '1'),
('Maria Clara', '3214325434', '1'),
('Sergião (Jullius)', '3214325434', '1');

INSERT INTO 

livro (genero, titulo, dataPublicaçao, autor)
VALUES ('Terror', 'It: A Coisa',
DATE ('now'), 'Stephen King'),
('Comédia', 'Diario de um Bannana',
DATE ('now'), 'Jeff Kinney');

INSERT INTO emprestimo(valor, )