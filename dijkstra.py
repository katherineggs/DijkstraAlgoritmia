def dijkstra(info, origin, destiny):
    path=[]
    camino = 0
    for nodo,arista in info.items():
        # verificar si existe un camino directo entre origen y destino
        if(origin == nodo):
            for k,value in arista.items():
                if(destiny == k):
                    if(value != -1):
                        path.append(value)

            keyNode = min(arista, key=arista.get)
            mini = arista[keyNode]
            camino = camino + mini
            origin = keyNode

            dijkstra(info,origin,destiny)
       

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
        aristas = {}
        for j in range(len(nodos)):
            if(i != j):
                num = int(input("Ingrese la conexion entre "+ str(nodos[i])+ " - "+ str(nodos[j]) +": " ))
                aristas[nodos[j]] = num
        info[nodos[i]] = aristas

    # origen y destino
    origin = int(input("Ingrese el origen: "))
    destiny = int(input("Ingrese a donde se dirige: "))
    
    # print(info)

    # origin = 1
    # destiny = 4
    
    # arista = {1:6, 2:3, 3:1}
    # key = min(arista, key=arista.get)
    # print(key)
    # print(arista[min(arista, key=arista.get)])


    dijkstra(info, origin, destiny)