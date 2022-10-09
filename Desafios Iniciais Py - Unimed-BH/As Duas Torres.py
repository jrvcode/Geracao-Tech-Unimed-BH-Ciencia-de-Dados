#As Duas Torres

entrada = input().split()

distancia = int(entrada[0])
diametro1 = int(entrada[1])
diametro2 = int(entrada[2])

saida = distancia / (diametro1 + diametro2)
print('%0.2f' % saida)
