# As Duas Torres
# Desafio 1/3:
# https://github.com/jrvcode/Geracao-Tech-Unimed-BH-Ciencia-de-Dados/blob/main/Desafios-Iniciais-Py-Unimed-BH/README.md

entrada = input().split()

distancia = int(entrada[0])
diametro1 = int(entrada[1])
diametro2 = int(entrada[2])

saida = distancia / (diametro1 + diametro2)
print('%0.2f' % saida)