# Aumento Salarial
# Desafio 3/3:
# https://github.com/jrvcode/Geracao-Tech-Unimed-BH-Ciencia-de-Dados/tree/main/Desafios-Intermediarios-Py-Unimed-BH#readme

salario = int(input()) 

if salario <= 600:
  novo = salario + (salario * 0.17)
  reajuste = salario * 0.17
  percentual = 17
elif salario >= 600.01 and salario <= 900:
  novo = salario + (salario * 0.13)
  reajuste = salario * 0.13
  percentual = 13
elif salario >= 900.01 and salario <= 1500:
  novo = salario + (salario * 0.12)
  reajuste = salario * 0.12
  percentual = 12
elif salario >= 1500.01 and salario <= 2000:
  novo = salario + (salario * 0.10)
  reajuste = salario * 0.10
  percentual = 10
else:
  novo = salario + (salario * 0.05)
  reajuste = salario * 0.05
  percentual = 5

print(f'Novo salario: {novo:.2f} \nReajuste ganho: {reajuste:.2f} \nEm percentual: {percentual} %')