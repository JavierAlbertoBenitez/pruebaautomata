def automata(cadena):
    transicciones = {
        'A': {'x': 'B', 'y': 'T', 'z': 'T'},
        'B': {'x': 'C', 'y': 'T', 'z': 'T'},
        'C': {'x': 'C', 'y': 'D', 'z': 'C'},
        'D': {'x': 'C', 'y': 'D', 'z': 'C'},
    }

    alfabeto = ['x', 'y', 'z']

    estado_actual = 'A'

    estados_finales = ["D"]

    for caracter in cadena:
        if caracter in transicciones[estado_actual]:
            estado_actual = transicciones[estado_actual][caracter]
        elif estado_actual == 'T':
            break

    if estado_actual in estados_finales:
        print('Cadena aceptada')
    else:
        print('Cadena NO aceptada')
