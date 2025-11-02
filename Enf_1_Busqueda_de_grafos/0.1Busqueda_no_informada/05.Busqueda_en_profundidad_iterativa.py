# busqueda en profundidad Iterativa
# esta busqueda es como una version mas lista de la profundidad limitada
# 1 primero intento con limite 1
# 2 si no lo encuentro, intento con limite 2
# 3 si no, intento con limite 3
# y asi voy subiendo el limite poco a poco
# esto sirve porque
# - no me voy super profundo desde el inicio (eso puede ser infinito)
# - pero tarde o temprano llego al objetivo si es alcanzable

def dfs_limitada(grafo, actual, objetivo, limite, camino=None):
    # esta funcion es igual que en el tema anterior (profundidad limitada)
    # intenta llegar al objetivo sin pasar el limite

    if camino is None:
        camino = [actual]  # camino que llevo hasta ahorita

    # si ya llegue al objetivo, regreso el camino
    if actual == objetivo:
        return camino

    # si ya no me queda profundidad permitida, paro aqui
    if limite == 0:
        return None

    # pruebo cada vecino desde el lugar actual
    for vecino in grafo.get(actual, []):
        # llamada recursiva bajando el limite
        resultado = dfs_limitada(
            grafo,
            vecino,
            objetivo,
            limite - 1,        # bajo uno al limite
            camino + [vecino]  # agrego el vecino al camino
        )

        # si encontre camino valido lo regreso
        if resultado is not None:
            return resultado

    # si ninguno funciono, regreso none
    return None

def profundidad_iterativa(grafo, inicio, objetivo, limite_max):
    # esta funcion hace la parte "iterativa"
    # intenta encontrar camino con limite 1
    # luego con limite 2
    # luego con limite 3
    # y sigue asi hasta limite_max
    # si lo encuentra antes de llegar al limite max, se detiene

    for limite in range(1, limite_max + 1):
        # intento con este limite
        camino = dfs_limitada(grafo, inicio, objetivo, limite)

        # si si encontro camino, ya lo regresamos
        if camino is not None:
            return camino, limite

    # si acabe todos los limites y nunca encontre nada
    return None, None

# ejemplo rapido
if __name__ == "__main__":
    # salon -> pasillo, patio
    # pasillo -> lab
    # patio -> cafeteria
    # lab -> servidor
    # cafeteria -> servidor
    # servidor -> (nada)
    grafo = {
        "salon": ["pasillo", "patio"],
        "pasillo": ["lab"],
        "patio": ["cafeteria"],
        "lab": ["servidor"],
        "cafeteria": ["servidor"],
        "servidor": []
    }

    # queremos ir de salon a servidor
    # dejamos que pruebe limites 1,2,3,4,5
    camino, limite_usado = profundidad_iterativa(
        grafo,
        "salon",
        "servidor",
        limite_max=5
    )

    print("camino de salon a servidor:", camino)
    print("limite que se necesito:", limite_usado)
    # ejemplo: puede salir ['salon','pasillo','lab','servidor'] con limite 3

    # segundo intento: buscamos algo que no existe
    camino2, limite2 = profundidad_iterativa(
        grafo,
        "salon",
        "estacionamiento",
        limite_max=5
    )

    print("\ncamino de salon a estacionamiento:", camino2)
    print("limite que se intento:", limite2)
    # si camino2 es none significa que no hay forma de llegar