# Alfabeto
# Desafio 1/3:
# https://github.com/jrvcode/Geracao-Tech-Unimed-BH-Ciencia-de-Dados/tree/main/Desafios-Intermediarios-Py-Unimed-BH#readme

letra = input().upper()
import string
numAlf = list(string.ascii_uppercase) 
print(numAlf.index(letra)+1)