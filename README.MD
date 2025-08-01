# Projeto de Testes Automatizados - SauceDemo

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Playwright](https://img.shields.io/badge/Playwright-1.38.0-purple)
![Pytest](https://img.shields.io/badge/Pytest-7.4.0-green)
![CI](https://img.shields.io/badge/CI-GitHub_Actions-orange)

---

## 📚 Sobre o projeto

Este projeto foi desenvolvido com o objetivo de estudo e prática de **testes automatizados** em uma aplicação web real — o site [SauceDemo](https://www.saucedemo.com).

O foco foi criar uma suíte de testes completa, organizada e escalável utilizando as melhores práticas atuais para automação com:

- **Python**: Linguagem de programação principal
- **Playwright**: Biblioteca para automação de navegadores com suporte multiplataforma e paralelismo
- **Pytest**: Framework robusto de testes para Python, facilitando organização, fixtures e parametrização
- **pytest-html**: Geração de relatórios HTML bonitos e detalhados
- **GitHub Actions**: Integração contínua para execução automática dos testes em pipelines CI/CD

---

## 🚀 Tecnologias e ferramentas utilizadas

| Ferramenta     | Versão | Descrição                              |
| -------------- | ------ | -------------------------------------- |
| Python         | 3.11+  | Linguagem de programação               |
| Playwright     | 1.38.0 | Automação de browser moderna           |
| Pytest         | 7.4.0  | Framework de testes                    |
| pytest-html    | 4.1.1  | Relatórios HTML para Pytest            |
| GitHub Actions | N/A    | Pipeline CI para execução automatizada |

---

## 📂 Estrutura do projeto

saucedemo-tests/
│
├── tests/
│ ├── test_login.py
│ ├── test_products.py
│ ├── test_cart.py
│ └── test_checkout.py
│
│
├── pages/
│ ├── login_page.py
│ ├── products_page.py
│ ├── cart_page.py
│ └── checkout_page.py
│
│
├── conftest.py
├── requirements.txt
├── pytest.ini
├── .github/
│ └── workflows/
│ └── playwright_ci.yml
└── README.md

---

## 🎯 Funcionalidades testadas

- **Login**

  - Login válido
  - Login com usuário bloqueado
  - Login com campos vazios
  - Login com senha incorreta

- **Página de Produtos**

  - Verificar carregamento dos produtos
  - Ordenação por nome e preço (A-Z, Z-A, baixo-alto, alto-baixo)
  - Adição e remoção de itens do carrinho

- **Carrinho**

  - Acessar o carrinho
  - Verificar itens adicionados
  - Continuar comprando (voltar à página de produtos)
  - Remover produtos do carrinho

- **Checkout**

  - Iniciar o checkout
  - Preencher dados de envio
  - Finalizar a compra
  - Cancelar a compra

- **Menu lateral**
  - Logout
  - Acessar página "About"
  - Resetar estado do app (limpar carrinho)

---

## ⚙️ Como configurar e executar localmente

### Pré-requisitos

- Python 3.11 ou superior instalado
- Git (opcional para clonar o projeto)

### Passos

1. Clone o repositório (ou baixe os arquivos)

```
git clone https://github.com/seu-usuario/saucedemo-tests.git
cd saucedemo-tests
```

2. Crie e ative um ambiente virtual (recomendado)

```
python -m venv venv

# Windows
venv\Scripts\activate
# Linux/macOS
source venv/bin/activate
```

3. Instale as dependências

```
pip install -r requirements.txt
```

4. Instale os navegadores do Playwright

```
playwright install
```

5. Execute todos os testes com relatório HTML

```
pytest --html=report.html --self-contained-html
```

6. Abra o relatório gerado report.html no seu navegador para análise detalhada

---

## 📦 Integração contínua com GitHub Actions

O projeto já possui pipeline configurado para rodar os testes automaticamente a cada push na branch main (ou outra configurada), com geração de relatório.

Arquivo: `.github/workflows/playwright_ci.yml`

Ele:

- Instala o Python e dependências
- Instala o Playwright e navegadores
- Executa os testes com relatório HTML
- Publica o relatório como artefato do workflow
