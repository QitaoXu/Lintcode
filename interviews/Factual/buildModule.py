from collections import deque 

class Solution:

    def buildModules(self, dependencies, targets):

        module_set = set() 

        if dependencies is None or len(dependencies) == 0 or not targets:
            return module_set 

        memo = {} 

        for target in targets:

            if target in module_set:
                print("not exe")
                continue 

            module_set = module_set.union(self.build_module_helper_memo(dependencies, target, memo))                

        return module_set 
    
    def build_module_helper_memo(self, dependencies, target, memo):

        if target in memo:
            return memo[target] 

        if target not in dependencies:
            memo[target] = set([target]) 
            return memo[target] 

        target_depends = set([target])   

        for dependency in dependencies[target]:

            target_depends = target_depends.union(self.build_module_helper_memo(dependencies, dependency, memo) )

        memo[target] = target_depends 

        return memo[target] 

    def buildModule(self, dependencies, target): 

        module_set = set([target]) 

        self.build_module_helper(dependencies, target, module_set) 

        graph = self.build_graph(dependencies, module_set) 

        return self.topo_sort(graph) 


    def build_module_helper(self, dependencies, target, module_set):

        if target not in dependencies:
            return 

        for dependency in dependencies[target]:

            module_set.add(dependency) 

            self.build_module_helper(dependencies, dependency, module_set) 

    def build_graph(self, dependencies, module_set):

        graph = {node : set() for node in module_set} 

        for neighbor in dependencies.keys():
            if neighbor not in module_set:
                continue 

            for node in dependencies[neighbor]:

                graph[node].add(neighbor) 

        return graph 

    def get_indegrees(self, graph):

        indegrees = {node : 0 for node in graph} 

        for node in graph:
            for neighbor in graph[node]:

                indegrees[neighbor] += 1 

        return indegrees 

    def topo_sort(self, graph):

        indegrees = self.get_indegrees(graph) 

        queue = deque() 

        for node in graph:

            if indegrees[node] == 0:
                queue.append(node) 

        order = [] 

        while queue:

            node = queue.popleft() 
            order.append(node) 

            for neighbor in graph[node]:

                indegrees[neighbor] -= 1 

                if indegrees[neighbor] == 0:
                    queue.append(neighbor) 

        return order 


dependencies = {} 

dependencies["factual-commons"] = ["apache-commons", "guava", "thrift"] 
dependencies["map-reduce"] = ["apache-commons", "hadoop"] 
dependencies["place-attach"] = ["factual-commons", "map-reduce"]
dependencies["hive"] = ["hadoop", "apache-commons"]
dependencies["hive-querier"] = ["hive", "factual-commons"]

solution = Solution() 

# target = "hive-querier" 
# targets = ["hive-querier", "factual-commons"]
targets = ["place-attach", "map-reduce"]

# result = solution.buildModule(dependencies, target)
result = solution.buildModules(dependencies, targets) 

print(result) 
print(len(result)) 