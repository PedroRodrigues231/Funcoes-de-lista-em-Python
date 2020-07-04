peso = (2.0, 3.0, 4.0)
lista = []
counter=1
for i in range(0,3):
  lista.append(float(input("Insira a {}° nota: ".format(counter))))
  counter+=1
elemento = 0
for i in range(0,3):
  elemento = elemento + (lista[i] * peso[i])
print("A média ponderada é {0:f}".format(elemento/6))