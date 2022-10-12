# Papagaio Poliglota
# Desafio 2/3:
# https://github.com/jrvcode/Geracao-Tech-Unimed-BH-Ciencia-de-Dados/tree/main/Desafios-Intermediarios-Py-Unimed-BH#readme

while True: 
    try:
        perna = input()
           
        if perna == "esquerda":
            print("ingles \n")
        elif perna == "direita":
            print("frances \n")
        elif perna == "nenhuma":
            print("portugues \n")
        elif perna == "ambas":
            print("caiu \n")
    except EOFError: 
        break