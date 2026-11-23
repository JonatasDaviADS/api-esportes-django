# 🏆 API Loja de Esportes — Django REST Framework + Swagger

API REST de uma loja de **artigos esportivos**, desenvolvida com **Django** e **Django REST Framework**, banco **MariaDB** (XAMPP) e documentação interativa **Swagger** gerada com **drf-spectacular**.

Atividade avaliativa da disciplina **Desenvolvimento de Serviços e APIs** — CST Análise e Desenvolvimento de Sistemas (Unisenac).

---

## 🧰 Tecnologias

| Ferramenta | Papel |
|---|---|
| `Python` + `venv` | linguagem e ambiente virtual isolado |
| `Django` | framework web (estrutura do projeto, ORM, migrações) |
| `djangorestframework` (DRF) | transforma o Django em API REST |
| `drf-spectacular` | gera o schema OpenAPI 3.0 e as páginas Swagger UI / ReDoc |
| `mysqlclient` | conecta o Python ao MySQL/MariaDB |
| `django-cors-headers` | libera o acesso de front-ends de outras origens (CORS) |
| `XAMPP` | MariaDB 10.4 (banco) + phpMyAdmin |

---

## 🗄️ Modelagem do banco

| Item | Nome |
|---|---|
| Banco | `loja_esportes` |
| Tabela | `artigos_esportivos` |
| Model (classe) | `ArtigoEsportivo` |

| Coluna | Tipo | Exemplo |
|---|---|---|
| `id` | `BIGINT` (PK, auto incremento) | `1` |
| `nome` | `VARCHAR(150)` | `Chuteira Predator` |
| `marca` | `VARCHAR(100)` | `Adidas` |
| `modelo` | `VARCHAR(100)` | `Elite FG` |
| `cor` | `VARCHAR(50)` | `Preta` |
| `valor` | `DECIMAL(10,2)` | `899.90` |
| `ano` | `INT` | `2025` |
| `modalidade` | `VARCHAR(50)` | `Futebol` |

> Regras de validação: `valor` maior que zero e `ano` entre 1900 e 2100.

---

## 📁 Estrutura

```
Projeto_Esportes
├── config/                  # configurações do projeto
│   ├── __init__.py          # ajuste para MariaDB 10.4 (XAMPP)
│   ├── settings.py          # apps, banco, CORS, DRF, Swagger
│   └── urls.py              # rotas principais + Swagger/ReDoc
├── core/                    # app dos artigos esportivos
│   ├── models.py            # tabela ArtigoEsportivo (ORM)
│   ├── serializers.py       # tradutor objeto <-> JSON + validações
│   ├── views.py             # CRUD + 5 filtros + documentação
│   ├── urls.py              # router do DRF
│   └── migrations/          # "receitas" de criação da tabela
├── database/
│   └── dados_iniciais.sql   # 15 artigos de exemplo
├── manage.py
├── requirements.txt
└── .gitignore
```

---

## 🚀 Como rodar

1. No XAMPP, ligue `Apache` e `MySQL`.
2. No phpMyAdmin, crie o banco:
```sql
   CREATE DATABASE IF NOT EXISTS loja_esportes CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```
3. No terminal, na pasta do projeto:
```powershell
   python -m venv venv
   .\venv\Scripts\activate
   pip install -r requirements.txt
   python manage.py migrate
```
4. No phpMyAdmin, rode o `INSERT` do arquivo `database/dados_iniciais.sql`.
5. Ligue o servidor:
```powershell
   python manage.py runserver
```
6. Acesse:

| Página | Endereço |
|---|---|
| Swagger UI | `http://127.0.0.1:8000/api/docs/` |
| ReDoc | `http://127.0.0.1:8000/api/redoc/` |
| Schema OpenAPI | `http://127.0.0.1:8000/api/schema/` |
| API navegável (DRF) | `http://127.0.0.1:8000/api/artigos/` |

---

## 🔗 Endpoints

### CRUD + busca por ID

| Método | Rota | Ação | Sucesso |
|---|---|---|---|
| `GET` | `/api/artigos/` | listar todos | `200` |
| `POST` | `/api/artigos/` | cadastrar | `201` |
| `GET` | `/api/artigos/{id}/` | **buscar por ID** | `200` |
| `PUT` | `/api/artigos/{id}/` | atualizar todos os campos | `200` |
| `PATCH` | `/api/artigos/{id}/` | atualizar alguns campos | `200` |
| `DELETE` | `/api/artigos/{id}/` | excluir | `204` |

### 5 endpoints personalizados

| # | Rota | Filtro |
|---|---|---|
| P1 | `/api/artigos/modalidade/{modalidade}/` | por esporte (parcial, ignora maiúsculas) |
| P2 | `/api/artigos/marca/{marca}/` | por marca (parcial, ignora maiúsculas) |
| P3 | `/api/artigos/cor/{cor}/` | por cor (parcial, ignora maiúsculas) |
| P4 | `/api/artigos/ano/{ano}/` | por ano exato (4 dígitos) |
| P5 | `/api/artigos/faixa-preco/?min=100&max=500` | por faixa de preço, ordenado do mais barato |

> ⚠️ Sempre termine a URL com `/`. Sem a barra, `POST`, `PUT` e `DELETE` dão erro.

### Exemplo de JSON (POST / PUT)

```json
{
  "nome": "Prancha de Surf",
  "marca": "Mormaii",
  "modelo": "Fish 5.8",
  "cor": "Branca",
  "valor": "1890.00",
  "ano": 2024,
  "modalidade": "Surf"
}
```

---

## 🧠 Conceitos aplicados

| Conceito | Resumo |
|---|---|
| **API REST** | cada recurso tem uma URL; a ação é definida pelo método HTTP |
| **CRUD** | Create, Read, Update, Delete |
| **ORM** | a tabela é descrita como classe Python; o Django gera o SQL |
| **Migração** | `makemigrations` escreve a receita; `migrate` executa no banco |
| **`class Meta` / `db_table`** | define o nome real da tabela (`artigos_esportivos`) |
| **Serializer** | converte objeto ⇄ JSON e valida os dados (`validate_<campo>`) |
| **ModelViewSet** | entrega o CRUD completo pronto |
| **`@action`** | cria endpoints extras no ViewSet |
| **Lookups** | `__icontains` (contém), `__gte` (>=), `__lte` (<=) |
| **Path x Query params** | `/marca/Nike/` (no caminho) x `?min=100&max=500` (após o `?`) |
| **`Decimal`** | número exato para dinheiro (`float` perde centavos) |
| **OpenAPI / Swagger** | padrão de documentação + página interativa para testar a API |
| **`@extend_schema`** | enriquece a documentação: tags, resumos, parâmetros |
| **CORS** | permite que front-ends de outra origem consumam a API |

### Códigos HTTP

| Código | Significado |
|---|---|
| `200 OK` | sucesso (GET, PUT, PATCH) |
| `201 Created` | registro criado (POST) |
| `204 No Content` | registro excluído (DELETE) |
| `301 / 302` | redirecionamento (barra final / raiz para o Swagger) |
| `400 Bad Request` | dado inválido (validação) |
| `404 Not Found` | rota ou registro inexistente |
| `500 Internal Server Error` | erro no servidor |

---

## 🛠️ Comandos usados

### Ambiente

| Comando | O que faz |
|---|---|
| `python -m venv venv` | cria o ambiente virtual |
| `.\venv\Scripts\activate` | ativa o ambiente |
| `pip install ...` | instala bibliotecas |
| `pip freeze \| Out-File -Encoding utf8 requirements.txt` | salva as dependências em UTF-8 |

### Django

| Comando | O que faz |
|---|---|
| `django-admin startproject config .` | cria o projeto **na pasta atual** (o `.` evita pasta duplicada) |
| `python manage.py startapp core` | cria o app |
| `python manage.py makemigrations` | gera a migração |
| `python manage.py migrate` | cria/altera as tabelas no banco |
| `python manage.py runserver` | liga o servidor (porta 8000) |
| `python manage.py spectacular --validate --file schema.yml` | valida a documentação OpenAPI |

### Git

| Comando | O que faz |
|---|---|
| `git init` | cria o repositório local |
| `git add .` / `git add arquivo` | prepara tudo / só um arquivo |
| `git status` | confere o que vai entrar no commit |
| `git commit -m "msg"` | salva uma versão |
| `git branch -M main` | nomeia o ramo principal |
| `git remote add origin URL` | liga ao GitHub |
| `git push -u origin main` / `git push` | primeiro envio / envios seguintes |
| `git show --numstat HEAD` | linhas alteradas no último commit |
| `git grep -n texto HEAD -- arquivo` | procura texto dentro de um arquivo versionado |

---

## ⚠️ Problemas resolvidos

| Problema | Causa | Solução |
|---|---|---|
| Arquivo `requeriments.txt` extra | erro de digitação no `>` | apagar com `Remove-Item` |
| Pasta `.venv` duplicada | criada automaticamente pelo VS Code | apagar e selecionar o interpretador `venv` |
| `requirements.txt` binário no Git (`- -` no `--numstat`) | `>` do PowerShell salva em UTF-16 | `Out-File -Encoding utf8` |
| `"DatabaseFeatures" is not defined` | faltava o `import` | adicionar o import de `...mysql.features` |
| `'django.db.beckends.mysql' isn't an available database backend` | erro de digitação | `backends` |
| Tabela criada como `core_artigoesportivo` | `class Meta` sem indentação (fora da classe) | recuar 4 espaços e gerar a migração `0002` |
| `has no attribute 'AutoShema'` | erro de digitação | `AutoSchema` |
| Django 6 recusa MariaDB 10.4 | versão antiga do XAMPP | ajuste em `config/__init__.py` |

---

## 👤 Autor

**Jonatas Davi Nascimento Abreu** — CST Análise e Desenvolvimento de Sistemas, Unisenac