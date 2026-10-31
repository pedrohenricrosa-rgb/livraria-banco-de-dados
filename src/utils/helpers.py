import os


def sql_str(valor):
    """Texto para concatenar em SQL (escapa aspas simples). Vazio vira NULL."""
    if valor is None or str(valor).strip() == "":
        return "NULL"
    return "'" + str(valor).replace("'", "''") + "'"


def limpar_tela():
    os.system("clear")


def pausar():
    input("\nPressione ENTER para continuar...")


def ler_texto(prompt, obrigatorio=True, atual=None):
    while True:
        sufixo = f" [{atual}]" if atual is not None else ""
        v = input(f"{prompt}{sufixo}: ").strip()
        if v == "" and atual is not None:
            return atual
        if v == "" and obrigatorio:
            print("  Campo obrigatorio.")
            continue
        return v


def ler_inteiro(prompt, atual=None, minimo=0):
    while True:
        sufixo = f" [{atual}]" if atual is not None else ""
        v = input(f"{prompt}{sufixo}: ").strip()
        if v == "" and atual is not None:
            return atual
        try:
            n = int(v)
            if n < minimo:
                print(f"  Informe um valor >= {minimo}.")
                continue
            return n
        except ValueError:
            print("  Informe um numero inteiro valido.")


def ler_decimal(prompt, atual=None):
    while True:
        sufixo = f" [{atual}]" if atual is not None else ""
        v = input(f"{prompt}{sufixo}: ").strip().replace(",", ".")
        if v == "" and atual is not None:
            return atual
        try:
            n = float(v)
            if n < 0:
                print("  Informe um valor positivo.")
                continue
            return round(n, 2)
        except ValueError:
            print("  Informe um numero valido (ex.: 39.90).")


def confirmar(pergunta):
    while True:
        r = input(f"{pergunta} (S/N): ").strip().upper()
        if r in ("S", "SIM"):
            return True
        if r in ("N", "NAO", "NÃO"):
            return False
        print("  Responda S ou N.")
