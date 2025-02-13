# Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km. Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km,
# e R$ 0,45 para viagens mais longas.
dis =int(input("quantos km vc deseja percorre? "))
if dis == 200:
    print("o preço ficou",(dis - 200) * 0.50)  
    print("Vinicius Haskel Wilbert") 
elif dis > 200:
    print("o preço ficou",(dis - 200) * 0.45)  
    print("Vinicius Haskel Wilbert") 