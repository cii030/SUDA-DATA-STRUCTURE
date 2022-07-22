from abc import ABCMeta, abstractmethod


class AbstractStack(metaclass=ABCMeta):
    """抽象栈类"""

    @abstractmethod
    def __init__(self):
        """创建一个空栈"""

    @abstractmethod
    def empty(self):
        """判断栈是否为空"""

    @abstractmethod
    def __len__(self):
        """求栈的长度"""

    @abstractmethod
    def push(self, item):
        """入栈一个元素"""

    @abstractmethod
    def pop(self):
        """出栈一个元素"""

    @abstractmethod
    def get_top(self):
        """读取栈顶元素"""
