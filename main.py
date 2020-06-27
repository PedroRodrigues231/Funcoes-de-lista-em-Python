def impressao(lista):
  print("\n")
  print(lista)

lista = ["Banana", "Maça", "Laranja"] # Declaração de lista
lista.clear() # Limpa a lista 
print(lista) # Imprime a lista vazia
#############################

lista_2 = ["Banana"] # Defino uma 2° lista
lista = lista_2.copy() # Copio os dados da segunda lista para a primeira. 
print(lista)

#############################

lista.append("Banana") # Adicionei essas 3 palavras na lista anterior. 
lista.append("Braço")
lista.append("Teste")
count = lista.count("Banana") #Contei quantas vezes a palavra "Banana" aparecia na lista e salvei em uma variável.
print("\n{}\nA palavra 'Banana' aparece {} vezes na lista.".format(lista,count)) # Imprimi a lista e a variável

#############################

lista.extend(lista_2) #Adiciono os elementos da lista_2 no fim da lista 1 
impressao(lista) # Função pra impressão, só ignora. Papo pra outra aula.

#############################

print("\nA palabra 'Teste' está na posição {} da lista".format(lista.index("Teste"))) #Retorna a posição que a palavra buscada está, caso exista mais de uma a primeira encontrada será exibida.

#############################

lista.insert(2, "Panda") #Inseri a palavra panda na posição 2 da lista, ou seja, o 3° elemento.
print("\n")
print(lista)

#############################

lista.pop(1) # Apaguei o elemento na posição 1, ou seja, o segundo elemento. 
print("\n")
print(lista)

#############################

lista.remove("Banana") # Removi a palavra "Banana" da lista.
print("\n")
print(lista)

#############################

lista.reverse() # Inverto a ordem da lista
impressao(lista)

#############################

lista.sort() # Organizo em ordem alfábetica 
impressao(lista) 

#############################