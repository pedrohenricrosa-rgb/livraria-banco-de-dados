from src.conexion.oracle_queries import OracleQueries
from src.utils import config

LARGURA = 50


def _linha(texto="", centro=False):
    texto = texto.center(LARGURA - 4) if centro else texto.ljust(LARGURA - 4)
    return f"# {texto} #"


def exibir():
    try:
        with OracleQueries() as db:
            total_autores = db.scalar("select count(1) total_autores from autores")
            total_livros = db.scalar("select count(1) total_livros from livros")
        contagens = [f"  1 - AUTORES: {total_autores}", f"  2 - LIVROS:  {total_livros}"]
    except Exception as e:
        contagens = ["  (nao foi possivel conectar ao banco)", f"  {str(e)[:40]}"]

    print("#" * LARGURA)
    print(_linha(config.NOME_SISTEMA, centro=True))
    print(_linha())
    print(_linha("TOTAL DE REGISTROS EXISTENTES"))
    for c in contagens:
        print(_linha(c))
    print(_linha())
    print(_linha("CRIADO POR: " + config.INTEGRANTES[0]))
    for nome in config.INTEGRANTES[1:]:
        print(_linha(" " * 12 + nome))
    print(_linha())
    print(_linha(f"DISCIPLINA: {config.DISCIPLINA}"))
    print(_linha(" " * 12 + config.SEMESTRE))
    print(_linha(f"PROFESSOR: {config.PROFESSOR}"))
    print("#" * LARGURA)
