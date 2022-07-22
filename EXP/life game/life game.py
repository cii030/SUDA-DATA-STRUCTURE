import numpy as np
import random
from PIL import Image


def game_of_life(matrix):
    neighbors = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]
    rows = len(matrix)
    cols = len(matrix[0])
    # 从矩阵复制一份到 copy_board 中
    copy_board = [[matrix[row][col] for col in range(cols)] for row in range(rows)]
    # 遍历面板每一个格子里的细胞
    for row in range(rows):
        for col in range(cols):
            # 对于每一个细胞统计其八个相邻位置里的活细胞数量
            live_neighbors = 0
            for neighbor in neighbors:
                r = (row + neighbor[0])
                c = (col + neighbor[1])
                # 查看相邻的细胞是否是活细胞
                if (rows > r >= 0) and (cols > c >= 0) and (copy_board[r][c] == 1):
                    live_neighbors += 1
            # 死亡的规则
            if copy_board[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                matrix[row][col] = 0
            # 复活的规则
            if copy_board[row][col] == 0 and live_neighbors == 3:
                matrix[row][col] = 1


def generate_image(matrix, count):
    """将生成的01矩阵改为图像"""
    list_result = []
    for i in matrix:
        for j in i:
            if j == 1:
                list_result.append(0)
            else:
                list_result.append(255)
    # 再利用numpy将列表包装为数组
    array1 = np.array(list_result)
    # 进一步将array包装成矩阵
    data = np.matrix(array1)
    # 重新reshape一个矩阵为一个方阵
    data = np.reshape(data, (500, 500))
    # 调用Image的formarray方法将矩阵数据转换为图像PIL类型的数据
    new_map = Image.fromarray(data)
    new_map = new_map.convert("RGB")
    new_map.save(f"pic{count}.jpg")


if __name__ == '__main__':
    a = np.zeros((500, 500))  # 生成一个矩阵
    num_of_1 = random.randint(30000, 35000)  # 初始矩阵中含有1的个数
    for _ in range(num_of_1):
        r = random.randint(0, 499)
        c = random.randint(0, 499)
        a[r][c] = 1
    generate_image(a, 0)
    count = 0
    while count <= 100:  # 生成100张图
        count += 1
        game_of_life(a)
        generate_image(a, count)
