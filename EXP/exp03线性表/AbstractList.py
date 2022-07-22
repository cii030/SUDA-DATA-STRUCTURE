from abc import ABCMeta, abstractmethod


class AbstractList(metaclass=ABCMeta):
    """抽象表类，metaclass=ABCMeta表示AbstractList类为ABCMeta的子类"""

    @abstractmethod
    def __init__(self):
        """初始化线性表"""

    @abstractmethod
    def empty(self):
        """判断表是否为空"""

    @abstractmethod
    def __len__(self):
        """返回表中元素的个数"""

    @abstractmethod
    def clear(self):
        """清空表"""

    @abstractmethod
    def insert(self, i, item):
        """在表中i号位置插入元素item"""

    @abstractmethod
    def remove(self, i):
        """删除i号位置的元素"""

    @abstractmethod
    def retrieve(self, i):
        """获取i号位置的元素"""

    @abstractmethod
    def replace(self, i, item):
        """用item替换表中i号位置的元素 """

    @abstractmethod
    def contains(self, item):
        """判断表中是否包含元素item"""

    @abstractmethod
    def traverse(self):
        """输出表中所有元素"""
