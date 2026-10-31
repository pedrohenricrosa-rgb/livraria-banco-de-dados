# Sistema de Livraria - Banco de Dados (2026/2)

CRUD em console (Python + Oracle) com tabelas **AUTORES** e **LIVROS** (1 autor : N livros).
Disciplina: Banco de Dados - Prof. Howard Roatti.

## Integrantes
- INTEGRANTE 1 Pedro Henrique Couto Rosa

## Estrutura
```
principal.py            # menu principal
sql/create_tables.sql   # criacao das tabelas, sequences e dados de exemplo
diagrama.mmd            # diagrama relacional (Mermaid) -> exportar para PDF/PNG
src/model  src/controller  src/conexion  src/sql  src/reports  src/utils
```

## Como executar (Linux / VM da disciplina)
1. Crie as tabelas: abra `sql/create_tables.sql` no SQL Developer (ou SQL*Plus) e execute.
2. Dependências:
   ```bash
   python3 -m venv .venv && source .venv/bin/activate
   pip install -r requirements.txt
   ```
3. Credenciais do Oracle:
   ```bash
   export ORACLE_USER=seu_usuario
   export ORACLE_PASSWORD=sua_senha
   export ORACLE_DSN=localhost:1521/XEPDB1
   ```
4. Rode: `python3 principal.py`

## Funcionalidades
Splash screen com contagem de registros; relatórios (agrupamento e junção); inserir, remover (com verificação de FK) e atualizar registros.
