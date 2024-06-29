# Recibe el número de casos
numero_de_casos = int(input())

# El for recorre los número de casos
for i in range(numero_de_casos):
    # Se crean las fracciones
    numerador_derecha = 1
    denominador_derecha = 0
    numerador_izquierda = 0
    denominador_izquierda = 1
    # Se crean las instrucciones de recorrido*
    numerador_actual = numerador_derecha + numerador_izquierda
    denominador_atual = denominador_derecha + denominador_izquierda
    
    # Se reciben los movimientos
    movimientos = input()
    
    # Se recorre cada uno de los movimientos
    for movimientosIndex in range(len(movimientos)):
        
        # Se crea la condicion, si dice rigth o si dice otra cosa (En este caso left)
        if(movimientos[movimientosIndex] == "R"):
            numerador_izquierda = numerador_actual
            denominador_izquierda = denominador_atual
        else:
            numerador_derecha = numerador_actual
            denominador_derecha = denominador_atual
        
        # Se ejecutan las instrucciones usando las fracciones guardadas en el anterior for*
        numerador_actual = numerador_derecha + numerador_izquierda
        denominador_atual = denominador_derecha + denominador_izquierda   
    
    # Impmir el resultado
    print(str(numerador_actual) + "/" + str(denominador_atual))