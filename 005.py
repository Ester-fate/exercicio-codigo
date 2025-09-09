"""
Um funcionário de um empresa recebe um aumento salarial anualmente

sabe-se que:
Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00.
Em 1996, o salário foi aumentado em 1,5% sobre o salário de ano anterior.
A partir de 1997, os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior.

Faça um programa que determine o salário atual desse funcionário.
Após concluir isto, altere o programa permiitndo que o usuário digite o salário inicial do funcionário e o percentual de aumento para cada ano.
"""

def new_func():
    salario = int(input("Digite o salario inicial:"))
    aumento = int(input("Digite a porcentagem do aumento:"))

    multiplicar = salario * aumento/100
    print(f"O aumento em 1996 é: {multiplicar}")

    aumento = int(input("Digite o valor final do aumento:"))
    multiplicar = aumento * 2
    print(f"O valor do aumento no ano de 1997 é: {multiplicar}")

for i in range(100):
    new_func()
