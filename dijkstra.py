import numpy
from string import ascii_letters

class Node:
    def __init__(self, node):
        self.nodeId = node
        self.adjacent = {}
        # infinity for all
        self.distance = 100
        # todos los nodos como si no sea han recorrido       
        self.visited = False  
        # anterior
        self.previous = None

    def addNext(self, siguiente, peso=0):
        # adjacent {sig: peso} 
        self.adjacent[siguiente] = peso

    def getConnections(self):
        # todas los nodos del dict
        return self.adjacent.keys()  

    def getId(self):
        # id del nodo
        return self.nodeId

    def getWeight(self, siguiente):
        # vvalue del dict
        return self.adjacent[siguiente]

    def setDistance(self, dist):
        # poner distancia
        self.distance = dist

    def getDistance(self):
        return self.distance

    def setPrevious(self, prev):
        # nodo anterior
        self.previous = prev

    def setVisited(self):
        # por si ya lo recorrimos
        self.visited = True

    def __str__(self):
        return str(self.nodeId) + "adj: " + str([x.nodeId for x in self.adjacent])

class Graph:
    def __init__(self):
        self.allNodes = {}
        self.cantNodos = 0

    def __iter__(self):
        return iter(self.allNodes.values())

    def addNode(self, node):
        self.cantNodos = self.cantNodos + 1
        newNode = Node(node)
        # agregar al dict
        self.allNodes[node] = newNode
        return newNode

    def getNode(self, num):
        if num in self.allNodes:
            return self.allNodes[num]
        else:
            return None

    def addEdge(self, origen, destino, cost=0):
        if origen not in self.allNodes:
            self.addNode(origen)
        if destino not in self.allNodes:
            self.addNode(destino)

        self.allNodes[origen].addNext(self.allNodes[destino], cost)
        self.allNodes[destino].addNext(self.allNodes[origen], cost)

    def getNodes(self):
        return self.allNodes.keys()

    def setAnterior(self, actual):
        self.previous = actual

    def getAnterior(self, actual):
        return self.previous

def bestPath(v, path):
    if v.previous:
        path.append(v.previous.getId())
        bestPath(v.previous, path)
    return

import heapq

def dijkstra(aGraph, origen, objetivo):
    print ("Dijkstra Algorithm")
    origen.setDistance(0)

    unvisited_queue = []
    for v in aGraph:
        unvisited_queue.append((v.getDistance(),v))
    print(unvisited_queue)
    
    unvisited_queue.sort(key=lambda tup: tup[0])

    # heapq.heapify(unvisited_queue)

    while len(unvisited_queue):
        # Pop a node with the smallest distance 
        uv = unvisited_queue.pop(0)
        actual = uv[1]
        actual.setVisited()

        #for next in v.adjacent:
        for next in actual.adjacent:
            # if visited, skip
            if next.visited:
                continue
            newDistance = actual.getDistance() + actual.getWeight(next)

            if int(newDistance) < int(actual.getWeight(next)):
                next.setDistance(newDistance)
                next.setPrevious(actual)
                print ('updated : actual = %s next = %s newDistance = %s' \
                        %(actual.getId(), next.getId(), next.getDistance()))
            else:
                print ('not updated : actual = %s next = %s newDistance = %s' \
                        %(actual.getId(), next.getId(), next.getDistance()))

        # Rebuild heap
        # 1. Pop every item
        while len(unvisited_queue):
            unvisited_queue.pop(0)
        # 2. Put all vertices not visited into the queue
        unvisited_queue = [(v.getDistance(),v) for v in aGraph if not v.visited]
        unvisited_queue.sort(key=lambda tup: tup[0])

        # heapq.heapify(unvisited_queue)
    
if __name__ == '__main__':

    g = Graph()
    abc = list(string.ascii_lowercase)

    # numero de nodos 
    cantNodos = int(input("Cuantos nodos desea: "))
    nodos = []
    for i in range(1,cantNodos+1):
        g.addNode(abc[i])

     for i in range(len(nodos)):
        for j in range(len(nodos)):
            if(i != j):
                num = int(input("Ingrese la conexion entre "+ str(nodos[i])+ " - "+ str(nodos[j]) +": " ))
                g.addEdge(str(nodos[i]),str(nodos[j]), num)  

    print ('Graph data:')
    for v in g:
        for w in v.getConnections():
            vid = v.getId()
            wid = w.getId()
            print ('( %s , %s, %3d)'  % ( vid, wid, v.getWeight(w)))

    origin = (input("Ingrese el nodo origen: "))
    destiny = (input("Ingrese a donde se dirige: "))

    dijkstra(g, g.getNode(origen), g.getNode(destino)) 

    objetivo = g.getNode(destino)
    path = [objetivo.getId()]
    bestPath(objetivo, path)
    print ('The shortest path : %s' %(path[::-1]))
