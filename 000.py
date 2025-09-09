"""
Faça um programa que peça dois números e imprima a soma
"""

def new_func():
    num1 = int(input("Digite um  numero:"))
    num2 = int(input("Digite outro numero:"))

    soma = num1 + num2
    print(f"A soma entre {num1} E {num2} é {soma}")

for i in range(100):
    new_func()
