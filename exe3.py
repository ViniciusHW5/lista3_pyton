# Peça ao usuário para inserir um número entre 10 e 20 (inclusive). Se ele inserir um número dentro desse intervalo, exiba a mensagem "Obrigado", caso contrário, exiba a mensagem
# "Resposta incorreta"
num1 = int(input("digite um numero entre 10 e 20: "))
if num1 > 20:
    print("Resposta incorreta")
elif num1 < 10:
    print("Resposta incorreta")
else:
    print("Obrigado")    

