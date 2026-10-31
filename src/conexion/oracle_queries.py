import os
import oracledb


class OracleQueries:
    """Conexao com o Oracle. Credenciais via variaveis de ambiente."""

    def __init__(self):
        self.user = os.getenv("ORACLE_USER", "SEU_USUARIO")
        self.password = os.getenv("ORACLE_PASSWORD", "SUA_SENHA")
        self.dsn = os.getenv("ORACLE_DSN", "localhost:1521/XEPDB1")
        self.conn = None
        self.cursor = None

    def connect(self):
        self.conn = oracledb.connect(user=self.user, password=self.password, dsn=self.dsn)
        self.cursor = self.conn.cursor()

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc, tb):
        self.close()

    def execute(self, sql):
        """INSERT/UPDATE/DELETE com commit."""
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception:
            self.conn.rollback()
            raise

    def fetch(self, sql):
        """Retorna (colunas, linhas)."""
        self.cursor.execute(sql)
        colunas = [c[0] for c in self.cursor.description]
        return colunas, self.cursor.fetchall()

    def scalar(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchone()[0]
