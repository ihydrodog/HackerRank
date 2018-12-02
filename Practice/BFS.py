class Graph:
    def __init__( self, n ):
        self.nodeCount = n
        self.adjacentNodes = {}

    def connect( self, f, t ):
        self.adjacentNodes.setdefault( f, set()).add( t )
        self.adjacentNodes.setdefault( t, set()).add( f )


    def find_all_distances(self, startNode):

        toBeVisited = []

        toBeVisited.append( (startNode, 0) )

        distances = {}

        while toBeVisited:
            curNode, distance = toBeVisited.pop( 0 )
            if curNode not in distances:
                distances[curNode] = distance

            for adjacent in self.adjacentNodes.get( curNode, [] ):
                if adjacent not in distances:
                    toBeVisited.append( (adjacent, distance+6 ) )

        # ret = []
        for i in range( self.nodeCount ):
            if i != startNode:
                v = distances.get(i, -1)
                print(v, end=' ' )
                # ret.append( distances.get(i, -1) )
        print('')
        # print( ret, sep=' ', end='', flush=True)




t = int(input())
for i in range(t):
    n,m = [int(value) for value in input().split()]
    graph = Graph(n)
    for i in range(m):
        x,y = [int(x) for x in input().split()]
        graph.connect(x-1,y-1)
    s = int(input())
    graph.find_all_distances(s-1)