# Sistema de Livraria - Banco de Dados (2026/2)

Aplicação de console (Python + Oracle) com CRUD e relatórios sobre as tabelas **AUTORES** e **LIVROS** (1 autor : N livros).
Disciplina: Banco de Dados - Prof. Howard Roatti.

## Integrante
- Pedro Henrique Couto Rosa

## Vídeo demonstrativo
https://www.youtube.com/COLE_AQUI_O_LINK_DO_VIDEO

## Diagrama relacional
![Diagrama relacional](diagrama_relacional.png)

Arquivos: `diagrama_relacional.png` e `diagrama_relacional.pdf` (código-fonte Mermaid em `diagrama.mmd`).

## Estrutura do repositório
```
principal.py              # script principal (menus)
requirements.txt          # dependências Python
sql/create_tables.sql     # criação das tabelas, sequences e dados de exemplo
diagrama_relacional.png   # diagrama relacional
src/model                 # classes das entidades (Autor, Livro)
src/controller            # classes controladoras (SQL concatenado, sem ORM)
src/conexion              # conexão com o Oracle
src/sql                   # consultas dos relatórios
src/reports               # execução dos relatórios
src/utils                 # menus, splash screen e funções auxiliares
```

## Como executar (Linux / VM da disciplina)

1. **Criar as tabelas:** abra `sql/create_tables.sql` no SQL Developer (ou SQL*Plus) e execute o script inteiro.
2. **Instalar as dependências:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
3. **Configurar a conexão com o Oracle:**
   ```bash
   export ORACLE_USER=seu_usuario
   export ORACLE_PASSWORD=sua_senha
   export ORACLE_DSN=localhost:1521/XEPDB1
   ```
4. **Executar:**
   ```bash
   python3 principal.py
   ```

## Funcionalidades
- **Splash screen** com total de registros por tabela e integrantes do grupo.
- **Relatórios:** livros e valor de estoque por autor (agrupamento), catálogo de livros com autor (junção) e livros por gênero (agrupamento).
- **Inserir registros** de autores e livros.
- **Remover registros**, com confirmação e verificação de chave estrangeira (autor com livros só é removido se o usuário aceitar remover os livros também).
- **Atualizar registros**, com exibição do registro atualizado.
