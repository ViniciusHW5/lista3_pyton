# Peça ao usuário para inserir sua cor favorita. Se ele digitar "vermelho", "VERMELHO" ou "Vermelho" exibem a mensagem "Eu também gosto de vermelho",
# caso contrário, exibem a mensagem "Eu não gosto de [cor], eu prefiro vermelho".
cor = input("digite sua cor favorita: ")
if cor == ("Vermelho"):
    print("eu tambem gosto de Vermelho")
    print("Vinicius Haskel Wilbert")    
elif cor == ("vermelho"):
    print("eu tambem gosto de vermelho")
    print("Vinicius Haskel Wilbert")       
elif cor == ("VERMELHO"):
    print("eu tambem gosto de VERMELHO")
    print("Vinicius Haskel Wilbert")    
else:
    print("eu não gosto do ",cor,"eu prefiro vermelho")
    print("Vinicius Haskel Wilbert")    