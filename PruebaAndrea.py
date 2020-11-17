
def Dijkstra(cantNodos, origen):
    # "dibujar" el grafo
    grafo = {}
    nodos = []
    for i in range(1, cantNodos + 1):
        nodos.append(i)
    
    for i in range(len(nodos)):
        aristas = {}
        for j in range(len(nodos)):
            if(i != j):
                peso = int(input("Ingrese el peso de la arista que une a los nodos: "+ str(nodos[i])+ " - "+ str(nodos[j]) +": " ))
                aristas[nodos[j]] = peso
        
        grafo[nodos[i]] = aristas
    
    # imprimir el grafo ya con datos
    print("\nGRAFO: ")
    print(grafo)


    # Encontrar el camino más corto
    actual = origen
    pesoMinimo = 0
    listaNodos = []
    pesoActual = []
    previo = []
    for nodo in grafo.items():
        listaNodos.append(nodo)
        
    while listaNodos:
        for nodo,arista in grafo.items():
            for k,value in arista.items():
                keyNode = min(arista, key=arista.get)
                pesoMinimo = arista[keyNode]

        listaNodos.remove(pesoMinimo)

        for nodo,arista in grafo.items():
            if(origen == nodo):
             #ingresamos a los vertices del nodo origen
             for k,value in arista.items():
                if(value != -1):
                    var = pesoActual[pesoMinimo] + value
                
            if(var < pesoActual[nodo]):
                pesoActual[nodo] = var
                previo[nodo] = pesoMinimo
    
    print("\nrespuesta: ")
    print(previo)
    


# MAIN
if __name__ == "__main__":
    # "Llenar" grafo
    cantNodos = int(input("Ingrese la cantidad de nodos: "))
    origen = int(input("Ingrese el origen: "))
    Dijkstra(cantNodos, origen)
    print("\n")

    
    