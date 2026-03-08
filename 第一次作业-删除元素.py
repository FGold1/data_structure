from typing import Any, Iterable


class DeleteItem:
    """
    从列表中删除元素
    """

    def __init__(self, iterable: Iterable[Any]):
        self.iterable = list(iterable)

    def delete(self, index_to_delete: int) -> list[Any]:
        """
        从列表中删除指定索引的元素
        :param index_to_delete: 要删除的索引
        """
        length_of_iterable: int = len(self.iterable)

        # 从前往后移动元素，覆盖要删除的元素
        for i in range(index_to_delete, length_of_iterable - 1):
            self.iterable[i] = self.iterable[i + 1]

        # 删除最后一个多余的元素
        self.iterable.pop()

        return self.iterable
