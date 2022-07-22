class Vertex:
    def __init__(self, data=None):
        """图的顶点类"""
        self.data = data


class DNGraphMatrix:
    """有向网的邻接矩阵类"""

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

    def dijkstra(self, source):
        # 存放最短路径长度
        distance = [self._arcs[source][i] for i in range(self._vertexNum)]
        # 存放到达i号顶点的最短路径中i号顶点的前驱
        pre = [source for i in range(self._vertexNum)]
        # 模拟S集合，记录顶点是否已求得最短路径，已在S中的顶点标记为True
        solved = [False for i in range(self._vertexNum)]
        solved[source] = True
        for count in range(self._vertexNum):
            # 找到一条以j为终点的最短路径
            j = self.findMinDist(solved, distance)
            for i in range(self._vertexNum):
                if not solved[i]:
                    if self._arcs[j][i] < float('inf') and distance[j] + self._arcs[j][i] < distance[i]:
                        distance[i] = distance[j] + self._arcs[j][i]
                        pre[i] = j
        self.printShortest(distance, pre, solved, source)

    def findMinDist(self, solved, distance):
        """找出当前最短路径的方法"""
        minDist = float('inf')
        i = 0
        j = 0
        while i < self._vertexNum:
            if not solved[i] and distance[i] < minDist:
                j = i
                minDist = distance[j]
            i = i + 1
        solved[j] = True
        return j

    def printShortest(self, distance, pre, solved, start):
        """最短路径输出方法"""
        path = []
        v = 0
        while v < self._vertexNum:
            if solved[v] and v != start:
                print('最短路径', end=' ')
                path.append(v)  # 添加路径终点
                former = pre[v]  # 获取前一个顶点的下标
                while former != start:
                    path.append(former)
                    former = pre[former]
                path.append(start)
                while len(path) > 1:
                    print(self._vertices[path.pop()].data, '->', end='')
                print(self._vertices[path.pop()].data, end='')
                print('，长度为：', distance[v])
            v = v + 1

    def floyd(self):
        # 生成最短路径长度矩阵D
        d = [[0 for i in range(self._vertexNum)] for i in range(self._vertexNum)]
        # 生成最短路径矩阵P
        p = [[-1 for i in range(self._vertexNum)] for i in range(self._vertexNum)]
        for i in range(self._vertexNum):
            for j in range(self._vertexNum):
                d[i][j] = self._arcs[i][j]
                if self._arcs[i][j] < float('inf') and i != j:
                    p[i][j] = i
                else:
                    p[i][j] = -1
        # 依次经过顶点k，判断加入顶点k是否可以得到顶点i刀顶点j的更短路径
        for k in range(self._vertexNum):
            for i in range(self._vertexNum):
                for j in range(self._vertexNum):
                    if i != j and d[i][k] + d[k][j] < d[i][j]:
                        d[i][j] = d[i][k] + d[k][j]
                        p[i][j] = p[k][j]
        self.printAllShortest(d, p)

    def printAllShortest(self, d, p):
        """每对顶点间最短路径的输出算法"""
        path = []
        for start in range(self._vertexNum):
            for end in range(self._vertexNum):
                # 存在路径，即start与end不同，且路径长度不为无穷大
                if d[start][end] < float('inf') and start != end:
                    print('顶点' + self._vertices[start].data + '到顶点' + self._vertices[end].data + '的最短路径：', end='')
                    # 将start至end的路径逆向存储在path的列表中
                    j = end
                    while j != start and j != -1:
                        path.append(j)
                        j = p[start][j]
                    path.append(start)
                    # 逆序输出path中的各个顶点
                    while len(path) > 1:
                        print(self._vertices[path.pop()].data, end='->')
                    print(self._vertices[path.pop()].data, end='')
                    print(',长度为：' + str(d[start][end]))


if __name__ == '__main__':
    g9 = DNGraphMatrix()
    edgeList = [('0', '1', 5), ('0', '2', 3), ('0', '4', 2),
                ('1', '2', 2), ('1', '3', 6), ('2', '1', 1),
                ('2', '3', 2), ('4', '1', 6), ('4', '2', 10), ('4', '3', 4)]
    for i in range(5):
        g9.addVertex(str(i))
    for edge in edgeList:
        g9.addEdge(edge[0], edge[1], edge[2])
    g9.dijkstra(0)
    print('---------------------')
    g9.floyd()
