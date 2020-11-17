
def Dijkstra(cantNodos, origen, destino):
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


    actual = origen
    # Lista de nodos para ir descartando los que ya se revisaron
    nodosActualesRevisados = []
    for nodo in grafo.items():
        nodosActualesRevisados.append(nodo)
    
    #Obtenemos los caminos
    caminos = []

    # ingresamos al nodo origen
    for nodo,arista in grafo.items():
        if(origen == nodo):
            #ingresamos a los vertices del nodo origen
            for k,value in arista.items():
                #verificamos si hay vertices directas al nodo destino y lo agregamos al listado de caminos
                if(destino == k):
                    if(value != -1):
                        caminos.append(value)
                        nodosActualesRevisados.remove[nodo] #eliminamos de la lista el nodo que ya se revisó

                    #si no hay un vertice directo entre el nodo origen y el nodo destino, 
                    else:
                        keyNode = min(arista, key=arista.get)
                        pesoMinimo = arista[keyNode]
                        actual = pesoMinimo
                        Dijkstra(cantNodos, actual, destino)


    
    print("\nPESOS: ")
    print(caminos)


# MAIN
if __name__ == "__main__":
    # "Llenar" grafo
    cantNodos = int(input("Ingrese la cantidad de nodos: "))
    origen = int(input("Ingrese el origen: "))
    destino = int(input("Ingrese el destino: "))
    Dijkstra(cantNodos, origen, destino)
    print("\n")

    
    