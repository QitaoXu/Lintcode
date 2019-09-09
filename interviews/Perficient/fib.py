class Fib: 

    def fibnacci(self, n, results):

        if n == 1:
            results.insert(0, 0)
            return 0

        if n == 2:
            results.insert(0, 1)
            return 1

        results.insert(0, self.fibnacci(n - 1, results) + self.fibnacci(n - 2, results)) 
        return self.fibnacci(n - 1, results) + self.fibnacci(n - 2, results)

fib = Fib()

results = [] 
fib.fibnacci(10, results)
print(results)