lista1=[2,8,6,7,5,9,4,6,8,1];

num=int(input("Ingrese un numero para buscar en la lista"))
cont=0
for i in range(len(lista1)):
 if num==lista1[i]:
  cont=cont+1

if cont>0:
  print("El numero",num,"se encuentra",cont,"veces en la lista")
else:
  print("El numero",num,"no se encuentra en la lista")
