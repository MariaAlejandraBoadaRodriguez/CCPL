casos = int(input())
ruedas = int(input())

while ruedas > 0:
    array = []
    for i in range(ruedas):
        fila = []
        print(fila)
        for j in range(1):
            columna = input()
            fila.append(columna)
        array.append(fila)
    ruedas = ruedas - 1
    print(array)
    print(ruedas)
        
    
    
    