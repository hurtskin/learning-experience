class new_STlink_elem(object):
    def __init__(self, item):
        self.item = item
        self._next = None


class SList(object):
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def length(self):
        """链表长度"""
        p = self._head
        count = 0
        while p != None:
            count = count + 1
            p = p._next
        return count

    def append(self, item):
        """向链表尾部添加元素"""
        node = new_STlink_elem(item)
        p = self._head
        if self.is_empty():
            """"如果链表是空链表"""
            self._head = node
        else:
            while p._next != None:
                p = p._next
            p._next = node

    def add(self, item):
        """向链表头部添加元素"""
        node = new_STlink_elem(item)
        node._next = self._head
        self._head = node

    def insert(self, position, item):
        """向链表中间插入元素"""
        if position <= 0:
            """如果是插入位置是第一个则执行头插"""
            self.add(item)
        elif position >= self.length():
            """如果插入位置是最后一个则执行尾插"""
            self.append(item)
        else:
            """中间插入"""
            p = self._head
            count = 0
            while count < position - 1:
                count += 1
                p = p._next
            node = new_STlink_elem(item)
            node._next = p._next
            p._next = node

    def find(self, item):
        """查询链表中指定数据的位置"""
        p = self._head
        count = 0
        while p is not None:
            if p.item == item:
                yield count
                count += 1
                p = p._next
                continue
            else:
                count += 1
                p = p._next

    def delete(self, position):
        """"移除链表中指定位置的数据"""
        if position >= self.length() or position < 0:
            return None
        p = self._head
        count = 0
        if position == self.length() - 1:
            while p._next._next is None:
                p = p._next
            p._next = None
        else:
            while count != position:
                p = p._next
                count += 1
            recycle_bin = p._next
            p._next = p._next._next
            recycle_bin = None

    def travel(self):
        """列表遍历"""
        p = self._head
        while p != None:
            print(p.item, end=" ")
            yield p.item
            p = p._next


    def find_value(self, item):
        """某个值是否存在"""
        p = self._head
        count = 0
        while p is not None:
            if p.item == item:
                return True
            else:
                p = p._next
                count += 1
        if count >= self.length():
            return False


if __name__ == "__main__":
    STList = SList()
    STList.append(4)
    STList.append(5)
    STList.append(6)
    STList.add(3)
    STList.add(2)
    STList.add(1)
    STList.travel()
    print(STList.length())
    STList.delete(5)
    STList.insert(1, 2)
    STList.travel()
    STList.find(2)
    print(STList.find_value(7))
    print(STList.find_value(4))
    pass
