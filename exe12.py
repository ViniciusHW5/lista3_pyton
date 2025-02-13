# Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar. Você deve poder calcular a soma (+), subtração (-), multiplicação (*) e divisão (/). 
# Exiba o resultado da operação solicitada. (usar ELIF)
num1 = float(input("Digite o primeiro número"))
num2 = float(input("Digite o segundo número"))
print("1-SOMA")
print("2-SUBTRAÇÃO")
print("3-MUTIPLICAÇÃO")
print("4-DIVISÂO")
escolha = int(input("Digite o número correpondente a opção desejada: "))
if escolha == 1:
    soma=num1+num2
    print("Resultado da soma: ",soma)
    