num = (input("Ingresa 3 numeros separados por un espacio: ").split())
numbers = [int(x) for x in num]


while len(numbers) != 3:
    num = (input("Ingresa 3 numeros separados por un espacio: ").split())
    numbers = [int(x) for x in num]

higher = max(numbers)
numbers.remove(higher)
lower = min(numbers)
numbers.remove(lower)

print("Maximo: " + str(higher) + ", Medio: " + str(numbers[0]) + ", Minimo: " + str(lower))

