from collections.abc import Sequence
from typing import Any
class Set:
    def __init__(self, iterable:Sequence[Any]=None):
        """
        :param iterable: 初始化的集合，去重
        """
        self.iterable = []
        if iterable is not None:
            for item in iterable:
                if item not in self.iterable:
                    self.iterable.append(item)

    def search(self,element:Any) -> bool:
        return element in self.iterable

    def insert(self,element:Any) -> bool:
        """
        在末尾插入一个元素
        :param element: 要插入的元素
        :return: 插入是否成功
        """
        for index,item in enumerate(self.iterable):
            if item == element:
                return False
        self.iterable.append(element)
        return True

    def delete(self,element:Any) -> bool:
        if element in self.iterable:
            self.iterable.remove(element)
            return True
        return False

class OrderedArrayInsert:
    def __init__(self, iterable:Sequence[Any]):
        self.iterable = list(iterable)
        self.len = len(self.iterable)
    def insert(self,element:Any) -> None:
        insert_index:int =self.len
        for index,item in enumerate(self.iterable):
            if element < item:
                insert_index = index
                break
        self.iterable.append("")
        for i in range(self.len, insert_index, -1):
            self.iterable[i] = self.iterable[i - 1]
        self.iterable[insert_index] = element
        self.len +=1