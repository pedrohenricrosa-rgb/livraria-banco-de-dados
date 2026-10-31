import os
from src.conexion.oracle_queries import OracleQueries

_DIR_SQL = os.path.join(os.path.dirname(__file__), "..", "sql")


def _ler(nome_arquivo):
    with open(os.path.join(_DIR_SQL, nome_arquivo), encoding="utf-8") as f:
        return f.read().strip()


def _imprimir_tabela(colunas, linhas):
    if not linhas:
        print("\n  (nenhum registro encontrado)")
        return
    linhas = [["" if v is None else str(v) for v in l] for l in linhas]
    larguras = [max(len(c), *(len(l[i]) for l in linhas)) for i, c in enumerate(colunas)]
    sep = "+-" + "-+-".join("-" * w for w in larguras) + "-+"
    print(sep)
    print("| " + " | ".join(c.upper().ljust(w) for c, w in zip(colunas, larguras)) + " |")
    print(sep)
    for l in linhas:
        print("| " + " | ".join(v.ljust(w) for v, w in zip(l, larguras)) + " |")
    print(sep)
    print(f"{len(linhas)} registro(s)")


class Relatorios:
    def _executar(self, arquivo, titulo):
        print(f"\n=== {titulo} ===")
        with OracleQueries() as db:
            colunas, linhas = db.fetch(_ler(arquivo))
        _imprimir_tabela(colunas, linhas)

    def livros_por_autor(self):
        self._executar("relatorio_livros_por_autor.sql", "LIVROS E VALOR DE ESTOQUE POR AUTOR")

    def catalogo(self):
        self._executar("relatorio_catalogo.sql", "CATALOGO DE LIVROS COM AUTOR")

    def por_genero(self):
        self._executar("relatorio_por_genero.sql", "LIVROS POR GENERO")
