
nodos = [1,2,3,4]
info={}
for i in range(len(nodos)):
    aristas = []
    for j in range(len(nodos)):
        if(i != j):
            num = int(input("Ingrese la conexion entre "+ str(nodos[i])+ " - "+ str(nodos[j]) +": " ))
            aristas.append(num)
    info[nodos[i]] = aristas

prueba = {1: [6, 2], 2: [6, -1], 3: [2, -1]}

def dijkstra(info):
    for nodo,arista in info.items():
        origin = nodo
        for a in arista:
            sValue = min(a)
            # chequear


        

if __name__ == "__main__":
    nodos = [1,2,3,4]
    info={}
    for i in range(len(nodos)):
        aristas = []
        for j in range(len(nodos)):
            if(i != j):
                num = int(input("Ingrese la conexion entre "+ str(nodos[i])+ " - "+ str(nodos[j]) +": " ))
                aristas.append(num)
        info[nodos[i]] = aristas

    prueba = {1: [6, 2], 2: [6, -1], 3: [2, -1]}

    dijkstra(prueba)