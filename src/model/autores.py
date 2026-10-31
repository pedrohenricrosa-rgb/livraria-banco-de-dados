class Autor:
    def __init__(self, id_autor=None, nome="", nacionalidade=""):
        self._id_autor = id_autor
        self._nome = nome
        self._nacionalidade = nacionalidade

    @property
    def id_autor(self): return self._id_autor
    @id_autor.setter
    def id_autor(self, v): self._id_autor = v

    @property
    def nome(self): return self._nome
    @nome.setter
    def nome(self, v): self._nome = v

    @property
    def nacionalidade(self): return self._nacionalidade
    @nacionalidade.setter
    def nacionalidade(self, v): self._nacionalidade = v

    def to_string(self):
        return f"Autor {self._id_autor} | Nome: {self._nome} | Nacionalidade: {self._nacionalidade or '-'}"
