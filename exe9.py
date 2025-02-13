# Escreva um programa que faça o cálculo do imposto de renda 2025. Consulte a tabela no site da Receita federal.
salario = float (input("digite seu salario: "))
if salario <=2259.20:
    print("vc não precisa pagar ")
    print("Vinicius Haskel Wilbert")
elif salario >= 2259.20 and salario <= 2876.65:
    imposto = salario * 0.075
    print("imposto que vc tera que pagar:",imposto,"reais")
    print("Vinicius Haskel Wilbert")
elif salario >=  2826.66 and salario <=  3751.05:
    imposto = salario * 0.15
    print("imposto que vc tera que pagar:",imposto,"reais")
    print("Vinicius Haskel Wilbert")
elif salario >=  3751.06 and salario <=  4664.68:
    imposto = salario * 0.225
    print("imposto que vc tera que pagar:",imposto,"reais")
    print("Vinicius Haskel Wilbert")
elif salario <=  4664.68 :
    imposto = salario * 0.275
    print("imposto que vc tera que pagar:",imposto,"reais")
    print("Vinicius Haskel Wilbert")