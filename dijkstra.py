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

    def addNext(self, next, weight=0):
        # adjacent {next: peso} 
        self.adjacent[next] = weight

    def getConnections(self):
        # todas los nodos del dict
        return self.adjacent.keys()  

    def getId(self):
        # id del nodo
        return self.node

    def getWeight(self, next):
        # peso del nodo
        return self.adjacent[next]

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