class MyQueue:
    # 队列初始化
    def __init__(self):
        self.elements = []  # 用list存储队列元素
        self.pointer = 0    # 队头位置

    # 获取队列中元素个数
    def size(self):
        return len(self.elements) - self.pointer
    
    # 判断队列是否为空
    def empty(self):
        return self.size() == 0

    # 在队尾添加一个元素
    def add(self, e):
        self.elements.append(e)

    # 弹出队首元素，如果为空则返回None
    def poll(self):
        if self.empty():
            return None
        self.pointer += 1
        return self.elements[self.pointer-1]