# coding：utf-8
class Node(object):
    """节点类"""

    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SingCycleChain(object):
    """单向循环链表"""

    def __init__(self, node=None):
        self.__head = node
        # 设置回环
        if node:
            node.next = node

    def is_empty(self):
        return self.__head == None

    def length(self):
        if self.is_empty():
            return 0
        cur = self.__head
        count = 1
        while cur.next != self.__head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        if self.is_empty():
            return
        cur = self.__head
        while cur.next != self.__head:
            print(cur.elem, end=" ")
            cur = cur.next
        # 退出循环，打印尾节点的元素
        print(cur.elem)
        print("")

    def add(self, item):
        """头插法"""
        node = Node(item)
        #两种情况
        #判断是否为空
        if self.is_empty():
            self.__head = node
            self.next = self.__head
        else:
            node.next = self.__head
        # 移到链表尾部，将尾部节点的next指向node
        
