select l.id_livro, l.titulo, a.nome as autor, l.genero, l.preco, l.estoque
from livros l
inner join autores a on a.id_autor = l.id_autor
order by a.nome, l.titulo
