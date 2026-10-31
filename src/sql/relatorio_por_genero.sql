select l.genero,
       count(1) as total_titulos,
       round(avg(l.preco), 2) as preco_medio
from livros l
group by l.genero
order by total_titulos desc
