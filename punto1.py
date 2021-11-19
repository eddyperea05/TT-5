import numpy as np
list1 = []
list2 = []

for i in range(3):
    list1.append(float(input("Ingrese un valor para la primera lista: ")))
    list2.append(float(input("Ingrese un valor para la segunda lista: ")))

scalarProduct = np.dot(list1,list2)
listProduct = np.cross(list1, list2)

print("El producto escalar de las listas es: " + str(scalarProduct))
print("El producto vectorial de las listas es: " + str(listProduct))