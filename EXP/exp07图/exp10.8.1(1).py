class Vertex:
    def __init__(self, data=None):
        """图的顶点类"""
        self.data = data


class UDNGraphMatrix:
    """无向网的邻接矩阵类"""

    def __init__(self, max_vertex=32):
        self._vertexNum = 0
        self._arcNum = 0
        self._vertices = [None for i in range(0, max_vertex)]
        self._arcs = [[float('inf') for i in range(0, max_vertex)] for j in range(0, max_vertex)]
        for i in range(max_vertex):
            self._arcs[i][i] = 0

    def addVertex(self, v):
        """增加一个顶点"""
        newVertex = Vertex(v)
        self._vertices[self._vertexNum] = newVertex
        self._vertexNum += 1

    def locateVertex(self, v):
        """获得指定顶点的编号"""
        for i in range(self._vertexNum):
            if v == self._vertices[i].data:
                return i
        return -1

    def addEdge(self, v, w, weight):
        """增加一条从顶点v到w的权值为weight的边"""
        i = self.locateVertex(v)
        if i == -1:
            self.addVertex(v)
            i = self._vertexNum - 1
        j = self.locateVertex(w)
        if j == -1:
            self.addVertex(w)
            j = self._vertexNum - 1
        self._arcs[i][j] = weight
        self._arcs[j][i] = weight
        self._arcNum += 1

    def create(self):
        """根据输入信息创建图"""
        n, e = input('请输入顶点数和边数：').split()
        print('请分别输入图的各个顶点: ')
        for i in range(int(n)):
            self.addVertex(input())
        print('请输入图的各条边的信息：（如A B 1）')
        for i in range(int(e)):
            a, b, weight = input().split()
            self.addEdge(a, b, float(weight))

    def degree(self, v):
        """求顶点的度"""
        i = self.locateVertex(v)
        count = 0
        for j in range(self._vertexNum):
            count += self._arcs[i][j] != 0 and self._arcs[i][j] != float('inf')
        return count

    def graph_out(self):
        """输出图的顶点和邻接矩阵"""
        print('该图的顶点为：')
        for i in range(0,self._vertexNum):
            print(self._vertices[i].data,end=' ')
        print()
        print('该图的邻接矩阵为：')
        for i in range(0, self._vertexNum):
            for j in range(self._vertexNum):
                if self._arcs[i][j] == float('inf'):
                    print('%4s' % ('#'), end=' ')
                else:
                    print('%4.0f' % (self._arcs[i][j]), end=' ')
            print()

    def firstAdjVertex(self, v):
        """得到顶点v的第一个邻接点"""
        for w in range(self._vertexNum):
            if self._arcs[v][w] == 1:
                return w
        return -1

    def nextAdjVertex(self, v, adjacent):
        """得到顶点v相对于adjacent的下一个邻接点"""
        for w in range(adjacent + 1, self._vertexNum):
            if self._arcs[v][w] == 1:
                return w
        return -1

    def visitVertex(self, v):
        """访问顶点的方法"""
        print(self._vertices[v].data, end='')

    def dfs(self, visited, v):
        self.visitVertex(v)
        visited[v] = True
        nextAdj = self.firstAdjVertex(v)
        while nextAdj != -1:
            if not visited[nextAdj]:
                self.dfs(visited, nextAdj)
            nextAdj = self.nextAdjVertex(v, nextAdj)

    def dfsTraverse(self):
        print('该图的深度优先搜索序列为：', end='')
        visited = [False for i in range(self._vertexNum)]
        for i in range(self._vertexNum):
            if not visited[i]:
                self.dfs(visited, i)


if __name__ == '__main__':
    g3 = UDNGraphMatrix()
    g3.addVertex('A')
    g3.addVertex('B')
    g3.addVertex('C')
    g3.addEdge('A', 'B', 1)
    g3.addEdge('A', 'C', 1)
    g3.addEdge('B', 'D', 1)
    g3.addEdge('D', 'E', 1)
    g3.addEdge('B', 'F', 1)
    g3.addEdge('E', 'F', 1)
    g3.graph_out()
    g3.dfsTraverse()
