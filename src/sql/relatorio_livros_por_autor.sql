select a.nome as autor,
       count(l.id_livro) as total_titulos,
       nvl(sum(l.estoque), 0) as total_exemplares,
       nvl(sum(l.preco * l.estoque), 0) as valor_estoque
from autores a
left join livros l on l.id_autor = a.id_autor
group by a.nome
order by valor_estoque desc
