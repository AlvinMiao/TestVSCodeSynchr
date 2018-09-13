# coding：utf-8

# class SingleLinkLi(object):
# 	"""docstring for SingleLinkLi"""
# 	def __init__(self, item):
# 		super(SingleLineTab, self).__item__()
# 		#数据区
# 		self.item = item
# 		#下一个节点的标识
# 		self.next = None


#定义一个节点类
class Node(object):
    '''节点构建构造函数包含两个属性，元素和next保存元素和下一个节点的内存地址'''

    def __init__(self, elem):
        #元素区
        self.elem = elem
        #下一个节点的标识
        self.next = None


class SingleLinkList(object):
    """单链表"""

    def __init__(self, node=None):
        #定义一个头节点的属性
        self.__head = node

    def is_empty(self):
        '''判断链表是否为空'''
        return self.__head == None

    def length(self):
        """链表长度"""
        #cur游标，移动遍历节点
        cur = self.__head
        count = 0
        while cur != None:
            count += 1
            #执行.next向后移动一个节点
            cur = cur.next
        return count

    def travel(self):
        """遍历链表"""
        cur = self.__head
        while cur != None:
            #打印游标所指元素
            print(cur.elem, end=" ")
            cur = cur.next
        print("")

    def add(self, item):
        """从头部添加元素，头插法"""
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append(self, item):
        """从尾部添加元素,尾插法"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        """指定位置增加节点
        :param pos 从0开始计数(指定插入位置)"""
        if pos <= 0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            pre = self.__head
            count = 0
            #当循环退出 pre指向pos-1
            while count < (pos - 1):
                pre = pre.next
                count += 1
            node = Node(item)
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        """删除节点"""
        cur = self.__head
        pre = None
        count = 0
        while cur != None:
            if cur.elem == item:
                #判断当前这个节点是否为头节点
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
            else:
                pre = cur
                cur = cur.next
                count += 1
        return count

    def search(self, item):
        """查找节点是否存在"""
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False


#Test
if __name__ == '__main__':
    ll = SingleLinkList()
    print(ll.is_empty())
    print(ll.length())

    ll.append(1)
    print(ll.is_empty())
    print(ll.length())

    for i in range(2, 7):
        ll.append(i)
    ll.travel()
