tupla = (2, 8, 6, 7, 84, 56, 12)
#tupla = (2, 5, 7, 9, 20, 45, 145, 236)
aux = 1
largoTupla=len(tupla)
for i in range(len(tupla)-1):
    if tupla[i] < tupla[i + 1]:
        aux += 1
print("Aux=", aux)
print("Largo tupla", largoTupla)
if aux == largoTupla:
    print("Esta ordenada la tupla")
else:
    print("No esta ordenada la tupla")
