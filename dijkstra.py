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
