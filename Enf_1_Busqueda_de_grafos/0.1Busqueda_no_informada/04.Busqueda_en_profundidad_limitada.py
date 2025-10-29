# busqueda en profundidad limitada
# la busqueda en profundidad normal (dfs) se mete lo mas hondo que pueda
# problema: a veces se puede ir demasiado lejos y nunca parar
# la idea de profundidad limitada es ponerle un tope
# ejemplo: solo puedes bajar 2 niveles desde el inicio y ya
# si el objetivo esta muy lejos y el limite es chiquito, no lo va a encontrar
# si el limite es suficiente, si lo encuentra

def dfs_limitada(grafo, actual, objetivo, limite, camino=None):
    # grafo: conexiones entre lugares
    # actual: donde estoy ahorita
    # objetivo: a donde quiero llegar
    # limite: cuanta profundidad maxima puedo bajar
    # camino: el camino que llevo hasta ahorita

    # esta parte solo corre la primera vez para iniciar el camino
    if camino is None:
        camino = [actual]

    # si ya llegue al objetivo, regreso el camino
    if actual == objetivo:
        return camino

    # si ya me gaste todo el limite, ya no puedo bajar mas
    # entonces paro aqui y digo que por aqui no se llego
    if limite == 0:
        return None

    # si todavia tengo limite, intento avanzar con cada vecino
    for vecino in grafo.get(actual, []):
        # importante: le bajo 1 al limite
        resultado = dfs_limitada(
            grafo,
            vecino,
            objetivo,
            limite - 1,        # bajo un nivel de profundidad
            camino + [vecino]  # agrego el vecino al camino
        )

        # si encontre un camino valido, lo regreso
        if resultado is not None:
            return resultado

    # si ningun vecino funciono dentro del limite, regreso None
    return None

# ejemplo
if __name__ == "__main__":
    # salon va a pasillo y patio
    # pasillo va a lab
    # patio va a cafeteria
    # lab va a servidor
    # cafeteria va a servidor
    # servidor no va a otro lado
    grafo = {
        "salon": ["pasillo", "patio"],
        "pasillo": ["lab"],
        "patio": ["cafeteria"],
        "lab": ["servidor"],
        "cafeteria": ["servidor"],
        "servidor": []
    }
    # queremos ir de salon a servidor con distintos limites
    print("limite = 1")
    camino1 = dfs_limitada(grafo, "salon", "servidor", limite=1)
    print("  camino encontrado:", camino1)
    # con limite 1 solo puedo moverme una vez desde salon
    # salon -> pasillo o salon -> patio
    # pero todavia no alcanzo servidor

    print("\nlimite = 2")
    camino2 = dfs_limitada(grafo, "salon", "servidor", limite=2)
    print("  camino encontrado:", camino2)
    # con limite 2 puedo hacer salon -> pasillo -> lab
    # pero aun no llego a servidor

    print("\nlimite = 3")
    camino3 = dfs_limitada(grafo, "salon", "servidor", limite=3)
    print("  camino encontrado:", camino3)
    # con limite 3 ya puedo hacer salon -> pasillo -> lab -> servidor
    # aqui ya deberia encontrar un camino

    print("\nlimite = 3 pero objetivo raro (estacionamiento)")
    camino4 = dfs_limitada(grafo, "salon", "estacionamiento", limite=3)
    print("  camino encontrado:", camino4)
    # si sale None es porque no existe forma de llegar