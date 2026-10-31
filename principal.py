from src.controller.controller_autor import ControllerAutor
from src.controller.controller_livro import ControllerLivro
from src.model.autores import Autor
from src.model.livros import Livro
from src.reports.relatorios import Relatorios
from src.utils import config, splash_screen
from src.utils.helpers import (limpar_tela, pausar, ler_texto, ler_inteiro,
                               ler_decimal, confirmar)

ctrl_autor = ControllerAutor()
ctrl_livro = ControllerLivro()
relatorios = Relatorios()


def escolher(menu, maximo):
    print(menu)
    while True:
        r = input("Opcao: ").strip()
        if r.isdigit() and 0 <= int(r) <= maximo:
            return int(r)
        print("  Opcao invalida.")


def listar_autores():
    autores = ctrl_autor.listar()
    print("\n--- AUTORES ---")
    for a in autores:
        print(f"  {a.id_autor} - {a.nome}")
    return autores


def listar_livros():
    livros = ctrl_livro.listar()
    print("\n--- LIVROS ---")
    for l in livros:
        print(f"  {l.id_livro} - {l.titulo}")
    return livros


def escolher_autor(atual=None):
    autores = listar_autores()
    if not autores:
        print("  Nenhum autor cadastrado. Cadastre um autor primeiro.")
        return None
    while True:
        id_autor = ler_inteiro("ID do autor", atual=atual, minimo=1)
        if ctrl_autor.existe(id_autor):
            return ctrl_autor.buscar(id_autor)
        print("  Autor nao encontrado.")


# ---------- RELATORIOS ----------
def menu_relatorios():
    while True:
        limpar_tela()
        op = escolher(config.MENU_RELATORIOS, 3)
        if op == 0:
            return
        {1: relatorios.livros_por_autor, 2: relatorios.catalogo, 3: relatorios.por_genero}[op]()
        pausar()


# ---------- INSERIR ----------
def inserir_autor():
    print("\n--- NOVO AUTOR ---")
    a = Autor(nome=ler_texto("Nome"), nacionalidade=ler_texto("Nacionalidade (opcional)", obrigatorio=False))
    ctrl_autor.inserir(a)
    print("\nInserido com sucesso!\n" + a.to_string())


def inserir_livro():
    print("\n--- NOVO LIVRO ---")
    autor = escolher_autor()
    if autor is None:
        return
    l = Livro(titulo=ler_texto("Titulo"), genero=ler_texto("Genero"),
              preco=ler_decimal("Preco"), estoque=ler_inteiro("Estoque"), autor=autor)
    ctrl_livro.inserir(l)
    print("\nInserido com sucesso!\n" + l.to_string())


def menu_inserir():
    while True:
        limpar_tela()
        op = escolher(config.MENU_ENTIDADES, 2)
        if op == 0:
            return
        (inserir_autor if op == 1 else inserir_livro)()
        if not confirmar("\nDeseja inserir mais algum registro?"):
            return


# ---------- REMOVER ----------
def remover_autor():
    if not listar_autores():
        print("  Nenhum autor cadastrado.")
        return
    id_autor = ler_inteiro("ID do autor a remover", minimo=1)
    if not ctrl_autor.existe(id_autor):
        print("  Autor nao encontrado.")
        return
    print(ctrl_autor.buscar(id_autor).to_string())
    if not confirmar("Deseja realmente remover este autor?"):
        return
    total = ctrl_autor.total_livros(id_autor)
    em_cascata = False
    if total > 0:
        print(f"\n  Este autor possui {total} livro(s) cadastrado(s) (FK em LIVROS).")
        if not confirmar("  Deseja remover tambem os livros dele?"):
            print("  Operacao cancelada: o autor nao pode ser excluido enquanto tiver livros.")
            return
        em_cascata = True
    ctrl_autor.excluir(id_autor, em_cascata)
    print("Autor removido com sucesso!")


def remover_livro():
    if not listar_livros():
        print("  Nenhum livro cadastrado.")
        return
    id_livro = ler_inteiro("ID do livro a remover", minimo=1)
    if not ctrl_livro.existe(id_livro):
        print("  Livro nao encontrado.")
        return
    print(ctrl_livro.buscar(id_livro).to_string())
    if not confirmar("Deseja realmente remover este livro?"):
        return
    ctrl_livro.excluir(id_livro)
    print("Livro removido com sucesso!")


def menu_remover():
    while True:
        limpar_tela()
        op = escolher(config.MENU_ENTIDADES, 2)
        if op == 0:
            return
        (remover_autor if op == 1 else remover_livro)()
        if not confirmar("\nDeseja remover mais algum registro?"):
            return


# ---------- ATUALIZAR ----------
def atualizar_autor():
    if not listar_autores():
        print("  Nenhum autor cadastrado.")
        return
    id_autor = ler_inteiro("ID do autor a atualizar", minimo=1)
    a = ctrl_autor.buscar(id_autor) if ctrl_autor.existe(id_autor) else None
    if a is None:
        print("  Autor nao encontrado.")
        return
    print("\n(ENTER mantem o valor atual)")
    a.nome = ler_texto("Nome", atual=a.nome)
    a.nacionalidade = ler_texto("Nacionalidade", obrigatorio=False, atual=a.nacionalidade or "")
    ctrl_autor.atualizar(a)
    print("\nAtualizado com sucesso!\n" + ctrl_autor.buscar(id_autor).to_string())


def atualizar_livro():
    if not listar_livros():
        print("  Nenhum livro cadastrado.")
        return
    id_livro = ler_inteiro("ID do livro a atualizar", minimo=1)
    l = ctrl_livro.buscar(id_livro) if ctrl_livro.existe(id_livro) else None
    if l is None:
        print("  Livro nao encontrado.")
        return
    print("\n(ENTER mantem o valor atual)")
    l.titulo = ler_texto("Titulo", atual=l.titulo)
    l.genero = ler_texto("Genero", atual=l.genero)
    l.preco = ler_decimal("Preco", atual=l.preco)
    l.estoque = ler_inteiro("Estoque", atual=l.estoque)
    l.autor = escolher_autor(atual=l.autor.id_autor)
    ctrl_livro.atualizar(l)
    print("\nAtualizado com sucesso!\n" + ctrl_livro.buscar(id_livro).to_string())


def menu_atualizar():
    while True:
        limpar_tela()
        op = escolher(config.MENU_ENTIDADES, 2)
        if op == 0:
            return
        (atualizar_autor if op == 1 else atualizar_livro)()
        if not confirmar("\nDeseja atualizar mais algum registro?"):
            return


# ---------- PRINCIPAL ----------
def run():
    limpar_tela()
    splash_screen.exibir()
    pausar()
    while True:
        limpar_tela()
        op = escolher(config.MENU_PRINCIPAL, 4)
        try:
            if op == 0:
                print("\nEncerrando... ate logo!")
                return
            {1: menu_relatorios, 2: menu_inserir, 3: menu_remover, 4: menu_atualizar}[op]()
        except Exception as e:
            print(f"\nErro: {e}")
            pausar()


if __name__ == "__main__":
    run()
