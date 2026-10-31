from src.model.autores import Autor


class Livro:
    def __init__(self, id_livro=None, titulo="", genero="", preco=0.0, estoque=0, autor: Autor = None):
        self._id_livro = id_livro
        self._titulo = titulo
        self._genero = genero
        self._preco = preco
        self._estoque = estoque
        self._autor = autor  # associacao: instancia de Autor

    @property
    def id_livro(self): return self._id_livro
    @id_livro.setter
    def id_livro(self, v): self._id_livro = v

    @property
    def titulo(self): return self._titulo
    @titulo.setter
    def titulo(self, v): self._titulo = v

    @property
    def genero(self): return self._genero
    @genero.setter
    def genero(self, v): self._genero = v

    @property
    def preco(self): return self._preco
    @preco.setter
    def preco(self, v): self._preco = v

    @property
    def estoque(self): return self._estoque
    @estoque.setter
    def estoque(self, v): self._estoque = v

    @property
    def autor(self): return self._autor
    @autor.setter
    def autor(self, v): self._autor = v

    def to_string(self):
        nome_autor = self._autor.nome if self._autor else "-"
        return (f"Livro {self._id_livro} | Titulo: {self._titulo} | Genero: {self._genero} | "
                f"Preco: R$ {self._preco:.2f} | Estoque: {self._estoque} | Autor: {nome_autor}")
