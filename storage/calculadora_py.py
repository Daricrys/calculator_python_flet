# Arquivo: calculadora.py
# Descrição: Este script é uma calculadora básica em python com flet.
# Autor: [DariF.]
# Data de Criação: 14/09/2025
# Reestruturado por Gemini.

# --- Início do código da calculadora ---

import flet as ft
from flet import Colors
from decimal import Decimal
import re # Biblioteca para usar expressões regulares, que ajudam a tratar o cálculo

# lista de botões da calculadora, com informações sobre operadores, cores e fundo:
botoes = [
    {'operador': 'AC', 'fonte': Colors.BLACK, 'fundo': Colors.BLUE_GREY_100},
    {'operador': '±', 'fonte': Colors.BLACK, 'fundo': Colors.BLUE_GREY_100},
    {'operador': '%', 'fonte': Colors.BLACK, 'fundo': Colors.BLUE_GREY_100},
    {'operador': '/', 'fonte': Colors.WHITE, 'fundo': Colors.ORANGE},
    {'operador': '7', 'fonte': Colors.WHITE, 'fundo': Colors.WHITE24},
    {'operador': '8', 'fonte': Colors.WHITE, 'fundo': Colors.WHITE24},
    {'operador': '9', 'fonte': Colors.WHITE, 'fundo': Colors.WHITE24},
    {'operador': '*', 'fonte': Colors.WHITE, 'fundo': Colors.ORANGE},
    {'operador': '4', 'fonte': Colors.WHITE, 'fundo': Colors.WHITE24},
    {'operador': '5', 'fonte': Colors.WHITE, 'fundo': Colors.WHITE24},
    {'operador': '6', 'fonte': Colors.WHITE, 'fundo': Colors.WHITE24},
    {'operador': '-', 'fonte': Colors.WHITE, 'fundo': Colors.ORANGE},
    {'operador': '1', 'fonte': Colors.WHITE, 'fundo': Colors.WHITE24},
    {'operador': '2', 'fonte': Colors.WHITE, 'fundo': Colors.WHITE24},
    {'operador': '3', 'fonte': Colors.WHITE, 'fundo': Colors.WHITE24},
    {'operador': '+', 'fonte': Colors.WHITE, 'fundo': Colors.ORANGE},
    {'operador': '0', 'fonte': Colors.WHITE, 'fundo': Colors.WHITE24},
    {'operador': '.', 'fonte': Colors.WHITE, 'fundo': Colors.WHITE24},
    {'operador': '=', 'fonte': Colors.WHITE, 'fundo': Colors.GREEN},
]

# A classe `Calculator` encapsula toda a lógica e a interface da calculadora.
class Calculator:
    def __init__(self, page: ft.Page):
        self.page = page
        self.expression = '' # Armazena a expressão matemática
        self.setup_page()
        self.create_ui()

    def setup_page(self):
        self.page.bgcolor = '#000'
        self.page.window_resizable = False
        self.page.window_width = 250
        self.page.window_height = 380
        self.page.title = 'Calculadora'
        self.page.window_always_on_top = True

        # Opcional: Centraliza a janela na tela
        #self.page.window_center()

        # Atualiza a página para aplicar as configurações de tamanho
        self.page.update()

    # A função `calculate_expression` avalia a expressão de forma segura.
    def calculate_expression(self):
        try:
            # Substitui operadores de porcentagem e sinal negativo antes de avaliar.
            # Essa é uma forma mais segura e controlada de usar 'eval()'.
            expression_eval = self.expression.replace('±', '-').replace('%', '/100')
            
            # Usa `eval()` aqui, mas a sanitização acima minimiza riscos.
            # Para maior segurança, bibliotecas como `ast` ou `numexpr` são recomendadas.
            result = eval(expression_eval)
            
            # Formata o resultado para evitar números com muitas casas decimais.
            digits = min(abs(Decimal(result).as_tuple().exponent), 5)
            return format(result, f'.{digits}f')
        except (ValueError, ZeroDivisionError, SyntaxError):
            return 'Error'

    # A função `select` agora lida com a lógica de cada botão.
    def select(self, e):
        value = e.control.content.value
        
        # Lógica para limpar a tela
        if value == 'AC':
            self.expression = ''
            self.result.value = '0'
        
        # Lógica para o botão de igual (=)
        elif value == '=':
            self.result.value = self.calculate_expression()
            self.expression = self.result.value # Armazena o resultado para continuar o cálculo
            
        # Lógica para o botão de sinal (±)
        elif value == '±':
            # Inverte o sinal do último número da expressão.
            if self.expression and self.expression[-1].isdigit():
                last_number = re.split(r'([+\-*/])', self.expression)[-1]
                new_number = str(-float(last_number))
                self.expression = self.expression.rsplit(last_number, 1)[0] + new_number
                self.result.value = self.expression
        
        # Lógica para o botão de porcentagem (%)
        elif value == '%':
            # Converte o último número para porcentagem.
            if self.expression and self.expression[-1].isdigit():
                last_number = re.split(r'([+\-*/])', self.expression)[-1]
                new_number = str(float(last_number) / 100)
                self.expression = self.expression.rsplit(last_number, 1)[0] + new_number
                self.result.value = self.expression
        
        # Lógica para operadores
        elif value in ('+', '-', '*', '/'):
            # Se o último caractere for um operador, substitui pelo novo.
            if self.expression and self.expression[-1] in ('+', '-', '*', '/'):
                self.expression = self.expression[:-1] + value
            else:
                self.expression += value
            self.result.value = self.expression
        
        # Lógica para dígitos e ponto decimal
        else:
            self.expression += value
            self.result.value = self.expression

        self.page.update()

    def create_ui(self):
        self.result = ft.Text(value="0", color=Colors.WHITE, size=20)
        
        btn_controls = []
        for btn_data in botoes:
            btn = ft.Container(
                content=ft.Text(value=btn_data['operador'], color=btn_data['fonte']),
                alignment=ft.alignment.center,
                width=50,
                height=50,
                bgcolor=btn_data['fundo'],
                border_radius=100,
                on_click=self.select
            )
            btn_controls.append(btn)

        display = ft.Row(
            width=250,
            controls=[self.result],
            alignment='end'
        )

        keyboard = ft.Row(
            width=250,
            wrap=True,
            controls=btn_controls,
            alignment='end'
        )

        self.page.add(display, keyboard)

# função principal para iniciar a aplicação:
def main(page: ft.Page):
    Calculator(page)

# Iniciar a aplicação
if __name__ == '__main__':
    ft.app(target=main)