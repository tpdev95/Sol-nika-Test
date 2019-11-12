num = (input("Ingresa 4 elementos separados por un espacio: ").split())
palindromos = []

while len(num) != 4:
    num = (input("Ingresa 4 numeros separados por un espacio: ").split())
    
    
for i in num:
    try:
        int(i)
        if str(i) == str(i)[::-1]:
            palindromos.append(i)
    except:
        pass

palindromos.sort()
print("Los siguientes numeros son palindromos!: " + str(palindromos))
