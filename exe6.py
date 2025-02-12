# Pergunte a idade do usuário. Se tiver 16 anos ou mais, exiba a mensagem "Você pode votar", se tiver 18 anos, exiba a mensagem "Você pode aprender a dirigir", 
# se tiver 14 anos, exiba a mensagem "Você pode comprar um bilhete de loteria", se tiver menos de 14 anos, exiba a mensagem "Você pode fazer doces ou travessuras". 
num1 =  int(input('digite sua idade '))
if num1 >=18:
    print("Você pode aprender a dirigir:")
else:    
    if num1 >=16:
        print("Você pode votar:")
    else:
         print("Você pode fazer doces ou travessuras:")  