# Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, de 15%.
salario = float(input("digite seu salario "))
if salario > 1250:
    print("seu salario foi aumentado em 10%:",(salario * 0.10)+salario,"R$")
    print("Vinicius Haskel Wilbert")    
if salario <= 1250:
    print("seu salario foi aumentado em 15%:",(salario * 0.15)+salario,"R$")
    print("Vinicius Haskel Wilbert")    
