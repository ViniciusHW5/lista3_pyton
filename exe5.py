# Pergunte ao usuário se está chovendo e converta sua resposta em minúsculas para que não importe em que caso ele digite. Se ele responder "sim", 
# pergunte se está ventando. Se ele responder "sim" a esta segunda pergunta, exiba a resposta "Está ventando muito para um guarda-chuva", caso contrário, 
# exiba a mensagem "Pegue um guarda-chuva". Se ele não respondera sim à primeira pergunta, mostre a resposta "Aproveite o seu dia". 
clima = input("Está chovendo?: ").strip().lower()
if clima =="sim":
    clima = input("esta ventando?").strip().lower()
    if clima == "sim":
        print("está ventando muito pra um guarda-chuva.")
        print("Vinicius Haskel Wilbert")        
    else:
        print("pegue um guada-chuva.")
        print("Vinicius Haskel Wilbert")
else:
    print("Aproveite seu dia")
    print("Vinicius Haskel Wilbert")