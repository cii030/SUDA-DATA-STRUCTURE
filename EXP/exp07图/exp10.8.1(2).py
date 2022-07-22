from CircularQueue import CircularQueue


class Vertex:
    def __init__(self, data=None):
        self.data = data
        self.firstArc = None


class Arc:
    def __init__(self, adjacent, weight, next=None):
        self.adjacent = adjacent
        self.weight = weight
        self.nextArc = next


class UDNGraphAdjList:
    def __init__(self):
        self._vertexNum = 0
        self._arcNum = 0
        self._vertices = []

    def locateVertex(self, v):
        """获得指定顶点的编号"""
        for i in range(self._vertexNum):
            if v == self._vertices[i].data:
                return i
        return -1

    def addVertex(self, v):
        """增加一个顶点"""
        newVertex = Vertex(v)
        self._vertices.append(newVertex)
        self._vertexNum += 1

    def addEdge(self, v, w, weight):
        """增加一条边"""
        i = self.locateVertex(v)
        if i == -1:
            self.addVertex(v)
            i = self._vertexNum - 1  # v顶点的编号为当前顶点数减去1
        j = self.locateVertex(w)
        if j == -1:
            self.addVertex(w)
            j = self._vertexNum - 1
        edge_node1 = Arc(j, weight, self._vertices[i].firstArc)
        self._vertices[i].firstArc = edge_node1
        edge_node2 = Arc(i, weight, self._vertices[j].firstArc)
        self._vertices[j].firstArc = edge_node2
        self._arcNum += 1

    def graph_out(self):
        """输出无向网的邻接表"""
        for i in range(self._vertexNum):
            print(i, ':', self._vertices[i].data, end='')
            p = self._vertices[i].firstArc
            while p:
                print('->', p.adjacent, '|', p.weight, end=' ')
                p = p.nextArc
            print()

    def visitVertex(self, v):
        """访问顶点的方法"""
        print(self._vertices[v].data, end=' ')

    def firstAdjVertex(self, v):
        """求v号顶点的第一个邻接点的编号"""
        firstArc = self._vertices[v].firstArc
        if firstArc:
            return firstArc.adjacent
        else:
            return -1

    def nextAdjVertex(self, v, adjacent):
        """求v号顶点相对于adjacent的下一个邻接点的编号"""
        p = self._vertices[v].firstArc
        while p:
            if p.adjacent == adjacent:
                if p.nextArc:
                    return p.nextArc.adjacent
                else:
                    return -1
            else:
                p = p.nextArc

    def bfs(self, visited, v):
        q = CircularQueue()
        visited[v] = True
        self.visitVertex(v)
        q.append(v)
        while not q.empty():
            u = q.serve()
            nextAdj = self.firstAdjVertex(u)
            while nextAdj != -1:
                if not visited[nextAdj]:
                    self.visitVertex(nextAdj)
                    visited[nextAdj] = True
                    q.append(nextAdj)
                nextAdj = self.nextAdjVertex(u, nextAdj)

    def bfsTraverse(self):
        print('该图的广度优先搜索序列为：', end=' ')
        visited = [False for i in range(self._vertexNum)]
        for i in range(self._vertexNum):
            if not visited[i]:
                self.bfs(visited, i)


if __name__ == '__main__':
    g7 = UDNGraphAdjList()
    edgeList = [(0, 1), (0, 5), (1, 2), (2, 3),
                (2, 5), (4, 5), (4, 6), (4, 8),
                (5, 6), (5, 7), (6, 7)]
    for i in range(9):
        g7.addVertex(str(i))
    for edge in edgeList:
        g7.addEdge(str(edge[0],), str(edge[1]),1)
    g7.graph_out()
    g7.bfsTraverse()
