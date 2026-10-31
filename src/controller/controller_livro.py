from src.conexion.oracle_queries import OracleQueries
from src.controller.controller_autor import ControllerAutor
from src.model.livros import Livro
from src.utils.helpers import sql_str

_SELECT = ("select l.id_livro, l.titulo, l.genero, l.preco, l.estoque, l.id_autor "
           "from livros l ")


class ControllerLivro:
    def __init__(self):
        self.ctrl_autor = ControllerAutor()

    def _montar(self, row):
        id_livro, titulo, genero, preco, estoque, id_autor = row
        return Livro(id_livro, titulo, genero, float(preco), int(estoque), self.ctrl_autor.buscar(id_autor))

    def existe(self, id_livro):
        with OracleQueries() as db:
            return db.scalar("select count(1) from livros where id_livro = " + str(int(id_livro))) > 0

    def buscar(self, id_livro):
        with OracleQueries() as db:
            _, rows = db.fetch(_SELECT + "where l.id_livro = " + str(int(id_livro)))
        return self._montar(rows[0]) if rows else None

    def listar(self):
        with OracleQueries() as db:
            _, rows = db.fetch(_SELECT + "order by l.id_livro")
        return [self._montar(r) for r in rows]

    def inserir(self, livro: Livro):
        sql = ("insert into livros (id_livro, titulo, genero, preco, estoque, id_autor) values (seq_livros.nextval, "
               + sql_str(livro.titulo) + ", " + sql_str(livro.genero) + ", "
               + str(livro.preco) + ", " + str(int(livro.estoque)) + ", "
               + str(int(livro.autor.id_autor)) + ")")
        with OracleQueries() as db:
            db.execute(sql)
            livro.id_livro = db.scalar("select seq_livros.currval from dual")
        return livro

    def atualizar(self, livro: Livro):
        sql = ("update livros set titulo = " + sql_str(livro.titulo)
               + ", genero = " + sql_str(livro.genero)
               + ", preco = " + str(livro.preco)
               + ", estoque = " + str(int(livro.estoque))
               + ", id_autor = " + str(int(livro.autor.id_autor))
               + " where id_livro = " + str(int(livro.id_livro)))
        with OracleQueries() as db:
            db.execute(sql)

    def excluir(self, id_livro):
        with OracleQueries() as db:
            db.execute("delete from livros where id_livro = " + str(int(id_livro)))
