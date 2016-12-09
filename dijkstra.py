import sys

class Edge:
    def __init__(self, u, v, length):
        self.u = u
        self.v = v
        self.length = length
    def __str__(self):
        return "edge (" + str(self.u) + "," + str(self.v) + ")" 
        
class Node:
    def __init__(self, ID):
        self.ID = ID
        self.dist = sys.maxint
        self.prev = None
        self.path = ""
        self.examined = False
    def __str__(self):
        return "node " + str(self.ID) + ", distance: " + str(self.dist) + ", path: " + str(self.path)

#find unique nodes from the list of edges
def identifyNodes(edges):
    nodesIDs = []
    nodes = []
    for e in edges:
        if e.u not in nodesIDs:
            nodesIDs.append(e.u)
            nodes.append(Node(e.u))
        if e.v not in nodesIDs:
            nodesIDs.append(e.v)
            nodes.append(Node(e.v))
    return nodes

def areNodesNeighbors(edges, node1, node2):
    result = False
    length = None
    for edge in edges:
        if (edge.v == node1.ID and edge.u == node2.ID) or (edge.v == node2.ID and edge.u == node1.ID):
            result = True
            length = edge.length
    return (result, length)

def dijkstra(edges, source, targets):
    nodes = identifyNodes(edges)
    n = len(nodes)
    for node in nodes:
        if node.ID == source:
            node.dist = 0
            break
    while n > 0:
        minDist = sys.maxint
        minNode = Node(-1)
        for node in nodes:
            if node.examined == False and node.dist < minDist:
                minDist = node.dist
                minNode = node
        for node in nodes:
            if node.ID == minNode.ID:
                node.examined = True
        n -= 1
        for node in nodes:
            (nodesAreNeighbors, length) = areNodesNeighbors(edges, node, minNode)
            if nodesAreNeighbors:
                alt = minNode.dist + length
                if alt < node.dist:
                    node.dist = alt
                    node.prev = minNode
                    node.path = minNode.path
                    node.path += ", " + str(minNode.ID)
    for node in nodes:
        if node.ID != source:
            node.path = node.path[2:] + ", " + str(node.ID)
        else:
            node.path = str(node.ID)
    for node in nodes:
        if node.ID == source:
            print "Source: " + str(node)
    for node in nodes:
        if node.ID in targets:
            print "Destination: " + str(node)

#edges = [Edge(1,2,5), Edge(2,3,6), Edge(1,3,13)]
#dijkstra(edges, 3, [1])

edges = [Edge(1,2,44), Edge(1,3,27), Edge(1,6,6), Edge(2,3,13), Edge(2,4,41), Edge(3,5,12), Edge(3,8,14), Edge(4,5,18), Edge(4,14,28), Edge(5,13,23), 
Edge(6,7,7), Edge(6,10,6), Edge(7,8,12), Edge(7,12,44), Edge(8,12,32), Edge(9,10,8), Edge(9,36,144), Edge(10,11,22), Edge(11,15,27), Edge(11,17,22), 
Edge(12,13,7), Edge(12,15,9), Edge(12,19,28), Edge(13,20,35), Edge(14,16,8), Edge(14,26,54), Edge(15,18,16), Edge(16,20,33), Edge(16,21,25), Edge(17,18,27), 
Edge(17,22,16), Edge(18,23,6), Edge(19,20,11), Edge(19,23,15), Edge(20,24,12), Edge(20,25,31), Edge(20,27,31), Edge(21,24,13), Edge(21,26,20), Edge(22,23,20), 
Edge(22,29,59), Edge(23,25,10), Edge(24,27,23), Edge(24,28,22), Edge(25,27,28), Edge(26,28,25), Edge(26,32,42), Edge(26,37,33), Edge(27,28,16), Edge(27,29,18), 
Edge(28,30,14), Edge(29,31,30), Edge(30,31,7), Edge(30,32,16), Edge(31,32,16), Edge(31,33,5), Edge(32,37,23), Edge(33,34,51), Edge(34,35,55), Edge(35,36,23)]
dijkstra(edges, 1, [25,32,35])