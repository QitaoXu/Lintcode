from collections import deque 
class Solution:

    def findAnanagramDiff(self, source, target):

        if source is None or target is None:
            return -1 

        if len(source) != len(target):
            return -1 

        target_hash = self.get_hash(target)

        queue = deque()
        seen = set()

        queue.append(source)
        seen.add(source)

        step = -1 

        while queue:

            size = len(queue)

            step += 1 

            for _ in range(size):

                string = queue.popleft()

                string_hash = self.get_hash(string)

                if string_hash == target_hash:
                    return step 

                for neighbor in self.get_neighbors(string):

                    if neighbor in seen:
                        continue 

                    queue.append(neighbor)
                    seen.add(neighbor)

        return -1 

    def get_neighbors(self, string):

        res = [] 

        for i in range(len(string)):

            pre, post = string[:i], string[i + 1:]

            for c in "abcdefghijklmnopqrstuvwxyz":

                if c == string[i]:
                    continue 

                neighbor = pre + c + post 
                res.append(neighbor)

        return res 

    def get_hash(self, string):

        letter_to_count = {} 

        for c in string:

            letter_to_count[c] = letter_to_count.get(c, 0) + 1 

        return letter_to_count

class Solution2:

    def findAnanagramDiff(self, source, target):

        target_letter_to_count = [0 for _ in range(26)]
        # source_lettter_to_count = [0 for _ in range(26)]

        for c in target:
            target_letter_to_count[ord(c) - ord('a')] += 1 

        for c in source:
            target_letter_to_count[ord(c) - ord('a')] -= 1 

        diff = 0 

        for i in range(26):
            if target_letter_to_count[i] != 0:
                diff += abs(target_letter_to_count[i])

        return diff // 2 
        

a = "aaaa"
b = "bbbb"

# solution = Solution()
# print(solution.findAnanagramDiff(a, b))
solution2 = Solution2()
print(solution2.findAnanagramDiff(a, b))


        