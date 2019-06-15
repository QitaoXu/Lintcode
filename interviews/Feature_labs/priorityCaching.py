MOVE_IN_BAR = 5 
MOVE_OUT_BAR = 3 
DECREASE_RATE = 1 
ACCESS_BONUS = 2 

class Solution:

    def initialize(self, callLogs):
        timestamp_to_item_list = {} 
        timestamp_to_item_set = {}
        item_to_priority = {} 

        last_second = -1 

        for timestamp, item in callLogs:

            if last_second < timestamp:
                last_second = timestamp

            if timestamp not in timestamp_to_item_list:
                timestamp_to_item_list[timestamp] = [] 
                timestamp_to_item_set[timestamp] = set()

            timestamp_to_item_list[timestamp].append(item) 
            timestamp_to_item_set[timestamp].add(item)

            item_to_priority[item] = 0 # initialize priority as 0 

        return timestamp_to_item_list, timestamp_to_item_set, item_to_priority, last_second

    def priorityCaching(self, callLogs):

        timestamp_to_item_list, timestamp_to_item_set, \
        item_to_priority, last_second = self.initialize(callLogs)

        cache = set()

        time_point = 1 

        while time_point <= last_second:

            if time_point in timestamp_to_item_list:

                for item in timestamp_to_item_list[time_point]:
                    item_to_priority[item] += ACCESS_BONUS 

                    if item_to_priority[item] > MOVE_IN_BAR:
                        cache.add(item) 

                for item in item_to_priority.keys():
                    if item not in timestamp_to_item_set[time_point]:
                        item_to_priority[item] = max(0, item_to_priority[item] - DECREASE_RATE)

                        if item_to_priority[item] <= MOVE_OUT_BAR and item in cache:
                            cache.remove(item)
            else:
                
                for item in item_to_priority.keys():
                    
                    item_to_priority[item] = max(0, item_to_priority[item] - DECREASE_RATE)

                    if item_to_priority[item] <= MOVE_OUT_BAR and item in cache:
                        cache.remove(item)

            time_point += 1 

        return list(cache) if len(cache) > 0 else [-1]

solution = Solution()

callLogs = [[1, 1], [2, 1], [3, 1], [4, 2], [5, 2], [6, 2]]

print(solution.priorityCaching(callLogs))







        


