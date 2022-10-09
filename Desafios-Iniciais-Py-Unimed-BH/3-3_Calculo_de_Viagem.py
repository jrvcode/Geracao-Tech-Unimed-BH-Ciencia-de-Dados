# Cálculo de Viagem
# Desafio 2/3:
# https://github.com/jrvcode/Geracao-Tech-Unimed-BH-Ciencia-de-Dados/blob/main/Desafios-Iniciais-Py-Unimed-BH/README.md

valores = input().split()

t = int(valores[0])
v = int(valores[1])

kml = 12

km = t * v
l = km / kml

print('%0.3f' % l)