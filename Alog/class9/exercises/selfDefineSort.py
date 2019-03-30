# class Interval:
#     def __init__(self, left, right):
#         self.left = left
#         self.right = right

#     # 以下为重写的__lt__方法
#     def __lt__(self, other):
#         # 当两个Interval比较大小时，直接比较它们的left属性
#         return self.left < other.left

# 要传给sort函数的key方法，表示按照interval.left进行排序
def IntervalKey(interval):
    return interval.left 

A = []
A.append(Interval(1, 7))
A.append(Interval(5, 6))
A.append(Interval(3, 4))
A.sort(key=IntervalKey)

class Interval:
    def __init__(self, left, right):
        self.left, self.right = left, right

    # 打印函数，用于直接print一个Interval对象
    def __repr__(self):
        return "Interval(%d, %d)" % (self.left, self.right)


data = [(3, 2), (3, 1), (2, 7), (1, 5), (2, 6), (1, 7)]
intervals = [Interval(left, right) for left, right in data]

print(sorted(intervals, key=lambda i: (i.left, i.right)))  # 先按x从小到大排，再按y从小到大排
# 结果: [Interval(1, 5), Interval(1, 7), Interval(2, 6), Interval(2, 7), Interval(3, 1), Interval(3, 2)]

print(sorted(intervals, key=lambda i: (-i.left, i.right)))  # 先按x从大到小排，再按y从小到大排
# 结果: [Interval(3, 1), Interval(3, 2), Interval(2, 6), Interval(2, 7), Interval(1, 5), Interval(1, 7)]

print(sorted(intervals, key=lambda i: (i.right, i.left)))  # 先按y从小到大排，再按x从小到大排
# 结果: [Interval(3, 1), Interval(3, 2), Interval(1, 5), Interval(2, 6), Interval(1, 7), Interval(2, 7)]

print(sorted(intervals, key=lambda i: (-i.right, i.left)))  # 先按y从大到小排，再按x从小到大排
# 结果: [Interval(1, 7), Interval(2, 7), Interval(2, 6), Interval(1, 5), Interval(3, 2), Interval(3, 1)]