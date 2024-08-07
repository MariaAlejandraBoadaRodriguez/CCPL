import re
n =  int(input())

while n > 0:
    palabra = input()
    palabras = input()
    print("Es x")
    print(len(palabra))
    lista_sin_caracteres = [re.sub('[^a-zA-Z0-9\s()]', '', string).strip() for string in palabras]
    filtrado = [elemento for elemento in lista_sin_caracteres if elemento != '']
    print("Es i")
    print(len(filtrado))
    
    i = 0
    x = 0

    while x < len(filtrado):
        print(x)
        print(filtrado)
        if palabras[i] == palabra[x]:
            print("palabra pequeña: " + filtrado[i])
            print("palabra gande: " + palabra[x])
            print("yes")
            i = i + 1
            x = x + 1
        else:
            print("palabra pequeña: " + filtrado[i])
            print("palabra gande: " + palabra[x])
            print("no")
            i = i
            print(i)
            x = x + 1
            print(x)
            
    n = n-1


