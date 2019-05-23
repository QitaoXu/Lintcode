class UinonFind:

    def __init__(self, n):

        self.father = [i for i in range(n + 1)]
        self.count = n 

    def union(self, a, b):

        root_a = self.find(a)
        root_b = self.find(b)

        if root_a == root_b:
            return True 

        self.father[root_b] = root_a 

        self.count -= 1 
        return False 

    def find(self, point):

        path = [] 

        while self.father[point] != point:
            
            path.append(point)
            point = self.father[point]

        for p in path:
            self.father[p] = point 

        return point 

class TravellingIsFun:

    def connectedCities(self, n, g, originCities, destinationCities):

        uf = UinonFind(n)

        q = len(originCities)
        res = [ 0 for _ in range(q)]

        for i in range(1, n):
            for j in range(i + 1, n + 1):

                # print(str(i) + "," + str(j) + "\t")

                if self.gcd(i, j) > g:
                    uf.union(i, j)

        for i in range(q):
            
            if uf.union(originCities[i], destinationCities[i]):
                res[i] = 1 
        return res 

    def gcd(self, a, b):
        if a < b:
            return self.gcdHelper(a, b)

        else:
            return self.gcdHelper(b, a)

    def gcdHelper(self, small, big):

        if big % small == 0:
            return small 

        else:
            return self.gcdHelper(big % small, small)

n = 6 
g = 1 
originCities = [1, 2, 4, 6]
destinationCities = [3, 3, 3, 4]

travelling = TravellingIsFun()

print(travelling.connectedCities(n, g, originCities, destinationCities))