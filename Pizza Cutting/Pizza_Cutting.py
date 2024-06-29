#Mientras sea verdadero el bucle
while True:
    # n recibe un numero y lo convierte a entero
    n = int(input())
    # Se comprueba si n es menor a 0
    if n < 0:
        # Si n es menor a 0 se rompe el ciclo
        break
    # Imprime la ecucación 
    print(n*(n+1)//2+1)
