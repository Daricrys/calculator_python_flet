# Calculadora Flet

![Flet](https://img.shields.io/badge/Flet-0.28.3-blue)
![Python](https://img.shields.io/badge/Python-3.13.2-yellow)
![Status do Projeto](https://img.shields.io/badge/status-andamento-orange)

## Descrição do Projeto

Este é um projeto de uma calculadora simples e funcional, criada com a biblioteca **Flet** em Python. A aplicação foi desenvolvida com o objetivo de testar os recursos do Flet para a criação de interfaces de usuário (UI) de forma rápida e eficiente.

A calculadora possui uma interface amigável com botões para operações básicas (+, -, *, /) e funções adicionais como porcentagem (%) e inversão de sinal (±).

## Funcionalidades

* **Interface Gráfica (GUI)**: Criada com Flet.
* **Operações Básicas**: Adição, subtração, multiplicação e divisão.
* **Funções Adicionais**: Porcentagem (%).
* **Design Responsivo**: O tamanho da janela é fixo e otimizado para desktop.
* **Lógica de Cálculo Robusta**: Lida com a substituição de operadores e formatação de resultados para evitar erros de ponto flutuante.

## Tecnologias Utilizadas

* **Python**: Linguagem de programação principal.
* **Flet**: Framework de UI para a construção da interface.

## Instalação e Execução

Para rodar este projeto em seu ambiente local, siga os passos abaixo:

1.  **Clone este repositório:**
    ```bash
    git clone [https://github.com/SeuUsuario/NomeDoSeuRepositorio.git](https://github.com/SeuUsuario/NomeDoSeuRepositorio.git)
    cd NomeDoSeuRepositorio
    ```

2.  **Crie e ative um ambiente virtual (recomendado):**
    ```bash
    # Para Windows
    python -m venv venv
    .\venv\Scripts\activate

    # Para macOS e Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install flet
    ```

4.  **Execute a aplicação:**
    ```bash
    flet run calculadora.py
    ```

## Empacotando como Executável

Se você deseja gerar um arquivo executável para a sua calculadora, use o comando `flet pack`. Certifique-se de que o Flet e o PyInstaller estão instalados em seu ambiente.

```bash
flet pack calculadora.py
