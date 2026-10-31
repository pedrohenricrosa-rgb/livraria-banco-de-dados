from src.conexion.oracle_queries import OracleQueries
from src.model.autores import Autor
from src.utils.helpers import sql_str


class ControllerAutor:
    def existe(self, id_autor):
        with OracleQueries() as db:
            return db.scalar("select count(1) from autores where id_autor = " + str(int(id_autor))) > 0

    def buscar(self, id_autor):
        with OracleQueries() as db:
            _, rows = db.fetch("select id_autor, nome, nacionalidade from autores where id_autor = " + str(int(id_autor)))
        return Autor(*rows[0]) if rows else None

    def listar(self):
        with OracleQueries() as db:
            _, rows = db.fetch("select id_autor, nome, nacionalidade from autores order by id_autor")
        return [Autor(*r) for r in rows]

    def inserir(self, autor: Autor):
        sql = ("insert into autores (id_autor, nome, nacionalidade) values (seq_autores.nextval, "
               + sql_str(autor.nome) + ", " + sql_str(autor.nacionalidade) + ")")
        with OracleQueries() as db:
            db.execute(sql)
            autor.id_autor = db.scalar("select seq_autores.currval from dual")
        return autor

    def atualizar(self, autor: Autor):
        sql = ("update autores set nome = " + sql_str(autor.nome)
               + ", nacionalidade = " + sql_str(autor.nacionalidade)
               + " where id_autor = " + str(int(autor.id_autor)))
        with OracleQueries() as db:
            db.execute(sql)

    def total_livros(self, id_autor):
        with OracleQueries() as db:
            return db.scalar("select count(1) from livros where id_autor = " + str(int(id_autor)))

    def excluir(self, id_autor, em_cascata=False):
        with OracleQueries() as db:
            if em_cascata:
                db.execute("delete from livros where id_autor = " + str(int(id_autor)))
            db.execute("delete from autores where id_autor = " + str(int(id_autor)))
