list = []

for i in range(5):
    list.append(input("Ingrese un carácter: "))

print("La lista original es: " + str(list))
list.reverse()
print("La lista invertida es: " + str(list))