# Escreva um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso,
# exiba o valor da multa, cobrando R$ 5 por km acima de 80 km/h.
velocidade =  int(input('qual é a velocidade do carro de um usuário: '))
if velocidade >=80:
    print("você foi multado ")
    print("Vinicius Haskel Wilbert")    
if velocidade >80:
    print("sua multa e R$"(velocidade - 80)* 5)
    print("Vinicius Haskel Wilbert")    

