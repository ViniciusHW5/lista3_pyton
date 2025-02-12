#Peça ao usuário para inserir um número inferior a 20. Se ele inserir um número 20 ou mais a mensagem "muito". caso contrário exiba "obrigado"
num1 = int(input("digite um numero inferior a 20: "))
if num1 > 20:
    print("muito")
elif num1 <=20:
    print("obrigado")  