#Peça dois número. Se o primeior for maior que o segundo. exiba primeiro o "segundo número" e depois o "primeiro número", caso contrário, mostre "primeio número" e "depois o segundo".
num1 = input("digite o primeiro numero: ")
num2 = input("digite o segundo numero: ")
if num1 < num2:
    print(num2)
    print(num1)
if num2 < num1:
    print(num1)
    print(num2)