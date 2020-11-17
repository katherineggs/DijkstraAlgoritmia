import sys

class Node:
    def __init__(self, node):
        self.node = node
        self.adjacent = {}
        # Set infinity for all
        self.distance = -1
        # All nodes unvisited        
        self.visited = False  
        # anterior
        self.previous = None

    def addNext(self, sig, weight=0):
        # adjacent {sig: peso} 
        self.adjacent[sig] = weight

    def getConnections(self):
        # todas los nodos del dict
        return self.adjacent.keys()  

    def getId(self):
        # id del nodo
        return self.node

    def getWeight(self, sig):
        # peso del nodo
        return self.adjacent[sig]

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
        return str(self.node) + ' next: ' + str([x.id for x in self.next])

class Graph:
    def __init__(self):
        self.allNodes = {}
        self.cantNodos = 0

    def __iter__(self):
        return iter(self.allNodes.values())

    def addNode(self, node):
        self.cantNodos = self.cantNodos + 1
        newNode = Node(node)
        self.allNodes[node] = newNode
        return newNode

    def getNode(self, num):
        if num in self.allNodes:
            return self.allNodes[num]
        else:
            return None

    def addEdge(self, origen, destino, peso = 0):
        if origen not in self.allNodes:
            self.addNode(origen)
        if destino not in self.allNodes:
            self.addNode(destino)

        self.allNodes[destino].addNext(self.allNodes[destino], peso)
        self.allNodes[destino].addNext(self.allNodes[destino], peso)

    def getNodes(self):
        return self.allNodes.keys()

    def setAnterior(self, actual):
        self.anterior = actual

    def getAnterior(self, actual):
        return self.anterior

def bestPath(v, path):
    if v.anterior:
        path.append(v.anterior.getId())
        bestPath(v.anterior, path)
    return

import heapq

def dijkstra(aGraph, origen, destino):
    print ("Dijkstra Algorithm")
    # Set the distance for the start node to zero 
    origen.setDistance(0)

    # Put tuple pair into the priority queue
    unvisited_queue = [(v.getDistance(),v) for v in aGraph]
    heapq.heapify(unvisited_queue)

    while len(unvisited_queue):
        # Pops a vertex with the smallest distance 
        uv = heapq.heappop(unvisited_queue)
        actual = uv[1]
        actual.setVisited()

        #for next in v.adjacent:
        for next in actual.next:
            # if visited, skip
            if next.visited:
                continue
            newDistance = actual.getDistance() + actual.getWeight(next)
            
            if int(newDistance) < int(next.getDistance()):
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
            heapq.heappop(unvisited_queue)
        # 2. Put all vertices not visited into the queue
        unvisited_queue = [(v.getDistance(),v) for v in aGraph if not v.visited]
        heapq.heapify(unvisited_queue)
    
if __name__ == '__main__':

    g = Graph()

    g.addNode('a')
    g.addNode('b')
    g.addNode('c')
    g.addNode('d')
    g.addNode('e')
    g.addNode('f')

    g.addEdge('a', 'b', 7)  
    g.addEdge('a', 'c', 9)
    g.addEdge('a', 'f', 14)
    g.addEdge('b', 'c', 10)
    g.addEdge('b', 'd', 15)
    g.addEdge('c', 'd', 11)
    g.addEdge('c', 'f', 2)
    g.addEdge('d', 'e', 6)
    g.addEdge('e', 'f', 9)

    print ('Graph data:')
    for v in g:
        for w in v.getConnections():
            vid = v.getId()
            wid = w.getId()
            print ('( %s , %s, %3d)'  % ( vid, wid, v.getWeight(w)))

    dijkstra(g, g.getNode('a'), g.getNode('e')) 

    target = g.getNode('e')
    path = [target.getId()]
    shortest(target, path)
    print ('The shortest path : %s' %(path[::-1]))