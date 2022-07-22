class Vertex:
    def __init__(self, data=None):
        """图的顶点类"""
        self.data = data


class CloseEdge:
    def __init__(self, lowcost, adjvertex):
        self.lowcost = lowcost
        self.adjvertex = adjvertex


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
        for i in range(0, self._vertexNum):
            print(self._vertices[i].data, end=' ')
        print()
        print('该图的邻接矩阵为：')
        for i in range(0, self._vertexNum):
            for j in range(self._vertexNum):
                if self._arcs[i][j] == float('inf'):
                    print('%4s' % ('#'), end=' ')
                else:
                    print('%4.0f' % (self._arcs[i][j]), end=' ')
            print()

    def prim(self, start):
        """求最小生成树算法"""
        print('组成最小生成树的边依次为：')
        # 初始化closeedges数组,closeedges[i].lowcost即为边(start,i)的权值
        # closeedges[i].adjvertex即为start
        closeedges = [None for i in range(self._vertexNum)]
        for i in range(self._vertexNum):
            closeedges[i] = CloseEdge(self._arcs[start][i], start)
        # 起点start的对应lowcost赋值为0，相当于置已加入生成树的标记
        closeedges[start].lowcost = 0
        for edge_no in range(1, self._vertexNum):
            # 调用getMin方法获得closeedges[i].lowcost中最小值对应的新顶点v
            v = self.getMin(closeedges)
            u = closeedges[v].adjvertex  # u为该最短边的已在生成树中的顶点
            # 输出一条生成树的边(u,v)
            print((self._vertices[u].data, self._vertices[v].data, self._arcs[u][v]))
            # 将v顶点的对应lowcost赋值为0，相当于置已加入生成树的标记
            closeedges[v].lowcost = 0
            # 更新其他顶点的closeedges值，如果边（v,i）的权值小于原closeedge[i].lowcost，
            # 则closeedges[i].lowcost更新为（v,i）的权值，closeedges[i].adjvertex更希望内v
            # 已加入生成树的顶点对应的lowcost值为0，if条件不成立，closeedges不更新
            for i in range(self._vertexNum):
                if self._arcs[v][i] < closeedges[i].lowcost:
                    closeedges[i] = CloseEdge(self._arcs[v][i], v)

    def getMin(self, closeedge):
        """求权值最小边"""
        v = 0
        minWeight = float('inf')
        for i in range(self._vertexNum):
            if closeedge[i].lowcost != 0 and closeedge[i].lowcost < minWeight:
                minWeight = closeedge[i].lowcost
                v = i
        return v


if __name__ == '__main__':
    g8 = UDNGraphMatrix()
    edgeList = [('0', '1', 4), ('0', '5', 2), ('0', '4', 3),
                ('1', '2', 2), ('1', '5', 6), ('2', '5', 5),
                ('2', '3', 6), ('3', '5', 3), ('3', '4', 7), ('4', '5', 1)]
    for i in range(6):
        g8.addVertex(str(i))
    for edge in edgeList:
        g8.addEdge(edge[0], edge[1], edge[2])
    g8.prim(0)
