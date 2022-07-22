class Vertex:
    def __init__(self, data):
        self.data = data


class UDGraphMatrix:
    def __init__(self, max_vertex=32):
        self._vertices = [None for i in range(0, max_vertex)]
        self._arcs = [[0 for i in range(0, max_vertex)]
                      for j in range(0, max_vertex)]
        self._arcNum = 0
        self._vertexNum = 0

    def addVertex(self, data):
        newVertex = Vertex(data)
        self._vertices[self._vertexNum] = newVertex
        self._vertexNum += 1

    def addEdge(self, v, w):
        i = self.locate_vertex(v)
        j = self.locate_vertex(w)
        self._arcs[i][j] = 1
        self._arcs[j][i] = 1
        self._arcNum += 1

    def locate_vertex(self, v):
        index = 0
        while self._vertices[index].data != v and \
                index < self._vertexNum:
            index = index + 1
        return index

    def firstAdjVertex(self, v):
        # 得到顶点v的第一个邻接点
        for w in range(self._vertexNum):
            if self._arcs[v][w] == 1:
                return w
        return -1

    def nextAdjVertex(self, v, adjacent):
        # 得到顶点v相对于adjacent的下一个邻接点
        for w in range(adjacent + 1, self._vertexNum):
            if self._arcs[v][w] == 1:
                return w
        return -1

    def path_len_n(self, a):
        visited = [0 for i in range(self._vertexNum)]  # 访问数组初始化
        way = []  # way记录路径
        self.dfs_path_len_n(a, way, visited)

    def dfs_path_len_n(self, u, path, visited):
        """求解u出发长度为n的路径放在path列表中并输出"""
        path.append(u)
        if len(path) == self._vertexNum:
            print(path)
        visited[u] = True
        k = self.firstAdjVertex(u)
        while k != -1:
            if not visited[k]:
                self.dfs_path_len_n(k, path, visited)
            k = self.nextAdjVertex(u, k)
        # 恢复该顶点的未访问标记，使得u在其它路径中可重新使用
        visited[u] = False
        path.pop()


if __name__ == "__main__":
    g = UDGraphMatrix()
    g.addVertex('0')
    g.addVertex('1')
    g.addVertex('2')
    g.addVertex('3')
    g.addVertex('4')
    g.addVertex('5')
    g.addVertex('6')
    g.addVertex('7')
    g.addVertex('8')
    g.addEdge('0', '1')
    g.addEdge('0', '5')
    g.addEdge('1', '2')
    g.addEdge('2', '3')
    g.addEdge('2', '5')
    g.addEdge('4', '5')
    g.addEdge('4', '6')
    g.addEdge('4', '8')
    g.addEdge('5', '6')
    g.addEdge('5', '7')
    g.addEdge('6', '7')
    g.addEdge('3', '8')
    start = int(input())
    g.path_len_n(start)
