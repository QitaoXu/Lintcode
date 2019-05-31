from collections import deque 

class Solution:

    def getLevelAverage(self, root):

        if not root:

            return [] 

        levels = [] 

        queue = deque()
        seen = set()

        queue.append(root)
        seen.add(root)

        while queue:

            level = [] 

            size = len(queue)

            for _ in range(size):

                node = queue.popleft()

                level.append(node.val)

                for neighbor in (node.left, node.right):

                    if neighbor is None:
                        continue 

                    queue.append(neighbor)
                    seen.add(neighbor)

            levels.insert(0, sum(level) // len(level))

        return levels

        