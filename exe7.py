# Peça ao usuário para inserir 1, 2 ou 3. Se ele inserir um 1, exiba a mensagem "Obrigado", se ele inserir um 2, exiba "Muito bem", se ele inserir um 3, exiba "Correto". 
# Se ele inserir qualquer outra coisa, exiba "Mensagem de erro".
num1 =  int(input('digite 1, 2 ou 3: '))
if num1 >=3:
    print("correto")
    print("Vinicius Haskel Wilbert")    
else:    
    if num1 >=2:
        print("Muito bem")
        print("Vinicius Haskel Wilbert")
    else:
     if num1 >=1:
        print("Obrigado")  
        print("Vinicius Haskel Wilbert")
     else:
         print("Mensagem de erro")  
         print("Vinicius Haskel Wilbert")