-- Sistema de Livraria - script de criacao (Oracle)
-- Execute no SQL Developer / SQL*Plus com o usuario da disciplina.

CREATE SEQUENCE seq_autores START WITH 1 INCREMENT BY 1 NOCACHE;
CREATE SEQUENCE seq_livros  START WITH 1 INCREMENT BY 1 NOCACHE;

CREATE TABLE autores (
    id_autor       NUMBER(10)    NOT NULL,
    nome           VARCHAR2(100) NOT NULL,
    nacionalidade  VARCHAR2(50),
    CONSTRAINT pk_autores PRIMARY KEY (id_autor)
);

CREATE TABLE livros (
    id_livro  NUMBER(10)    NOT NULL,
    titulo    VARCHAR2(150) NOT NULL,
    genero    VARCHAR2(50)  NOT NULL,
    preco     NUMBER(10,2)  NOT NULL,
    estoque   NUMBER(6)     DEFAULT 0 NOT NULL,
    id_autor  NUMBER(10)    NOT NULL,
    CONSTRAINT pk_livros PRIMARY KEY (id_livro),
    CONSTRAINT fk_livros_autores FOREIGN KEY (id_autor) REFERENCES autores (id_autor)
);

-- Dados de exemplo (opcional)
INSERT INTO autores VALUES (seq_autores.NEXTVAL, 'Machado de Assis', 'Brasileira');
INSERT INTO autores VALUES (seq_autores.NEXTVAL, 'Clarice Lispector', 'Brasileira');
INSERT INTO autores VALUES (seq_autores.NEXTVAL, 'George Orwell', 'Britanica');
INSERT INTO livros VALUES (seq_livros.NEXTVAL, 'Dom Casmurro', 'Romance', 39.90, 12, 1);
INSERT INTO livros VALUES (seq_livros.NEXTVAL, 'Memorias Postumas de Bras Cubas', 'Romance', 44.90, 8, 1);
INSERT INTO livros VALUES (seq_livros.NEXTVAL, 'A Hora da Estrela', 'Romance', 34.50, 5, 2);
INSERT INTO livros VALUES (seq_livros.NEXTVAL, '1984', 'Ficcao', 49.90, 20, 3);
COMMIT;
