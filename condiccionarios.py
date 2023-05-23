# Creo que la función automata que se comportara como el automata pedido.

def automata(cadena):
    # Creo un diccionario de diccionario, donde esta cada estado y la transiciones de los mismo dados un caracter
    transicciones = {
        'A': {'x': 'B', 'y': 'T', 'z': 'T'},
        'B': {'x': 'C', 'y': 'T', 'z': 'T'},
        'C': {'x': 'C', 'y': 'D', 'z': 'C'},
        'D': {'x': 'C', 'y': 'D', 'z': 'C'},
        'T': {}
    }

    # El estado actual arranca con el inicial el A
    estado_actual = 'A'

    # acá estan los estados finales para saber si es aceptado o no, en este caso será uno unico, pero creo una lista por si hay más de un estado aceptado
    estados_finales = ["D"]

    # Creo un ciclo que analice caracter por caracter la cadena ingresanda
    for caracter in cadena:
        # Consulta si el caracter se encuentra en las transicciones del estado actual.
        if caracter in transicciones[estado_actual]:
            # Si es así el estado actual será el estado al que lleva dicho caracter
            estado_actual = transicciones[estado_actual][caracter]
        else:
            # Si el caracter no es encuentra ahí cae al estado trampa y corta el ciclo
            estado_actual = 'T'
            break
    # Si el ultimo estado que llego el ciclo es un estado final, la cadena es aceptada
    if estado_actual in estados_finales:
        print('Cadena aceptada')
    else:
        # caso contrario no
        print('Cadena NO aceptada')
