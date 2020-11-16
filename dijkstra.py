
def dijkstra(info, origin, destiny):
    for nodo,arista in info.items():
        # verificar si existe un camino directo entre origen y destino
        origin = nodo
        for a in arista:
            sValue = min(a)
            # chequear


        

if __name__ == "__main__":
    # numero de nodos 
    cantNodos = int(input("Cuantos nodos desea: "))
    nodos = []
    for i in range(1,cantNodos+1):
        nodos.append(i)
# diccionario 
    # key = num nodo
    # value = lista de aristas en orden 
    info={}
    for i in range(len(nodos)):
        aristas = []
        for j in range(len(nodos)):
            if(i != j):
                num = int(input("Ingrese la conexion entre "+ str(nodos[i])+ " - "+ str(nodos[j]) +": " ))
                aristas.append(num)
        info[nodos[i]] = aristas
    # origen y destino
    origin = int(input("Ingrese el origen: "))
    destiny = int(input("Ingrese a donde se dirige: "))
    
    origin = 1
    destiny = 4
    
    prueba = {1: [6, 2], 2: [6, -1], 3: [2, -1]}

    dijkstra(prueba, origin, destiny)