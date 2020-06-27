nome = []
media = []
for i in range(0,3):
  soma = 0.0
  nome.append(input("Insira seu nome: ").title())
  for j in range(0,3):
    soma = soma + float(input("Insira a {}° sua nota: ".format(j+1)))
  media.append(soma/3)
for i in range(0,3):
  print("\n======\nNome = {}".format(nome[i]))
  print("Média = {}".format(media[i]))