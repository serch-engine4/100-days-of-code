print ("Problema 2. Fibonacci")
#Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
#         1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.


#función que define el siguiente elemento de la seria de fibonacci
def defineElementon(e1,e2):
	return e1 + e2

#primeros elementos de la seria
e1 = 1
e2 = 2
suma = e2

while (e2 < 4000000):
	en = defineElementon(e1,e2)
	e1 = e2
	e2 = en
	if (en<4000000 and ((en%2)==0)):
		suma = suma + en
		print(en)
print ("suma: " + str(suma))
print ("Fin")

