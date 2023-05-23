def automata(cadena):
    estado_actual = 'A'
    estado_finales = ['D']
    for caracter in cadena:
        if estado_actual == "A" and caracter == "x":
            estado_actual = 'B'
        elif estado_actual == "A" and (caracter == "y" or caracter == "z"):
            estado_actual = 'E'
        elif estado_actual == 'B' and caracter == "x":
            estado_actual = "C"
        elif estado_actual == 'B' and (caracter == "y" or caracter == "z"):
            estado_actual = "E"
        elif estado_actual == 'C' and caracter == 'y':
            estado_actual = 'D'
        elif estado_actual == 'C' and (caracter == 'x' or caracter == 'z'):
            estado_actual = 'C'
        elif estado_actual == 'D' and caracter == 'y':
            estado_actual = 'D'
        elif estado_actual == 'D' and (caracter == 'x' or caracter == 'z'):
            estado_actual = 'C'
        elif estado_actual == 'E':
            break
    if estado_actual in estado_finales:
        print('Es aceptada')
    else:
        print('No es aceptada')
