class Solution:

    def find_pairs(self, receipts, maxium_diff):

        points = [] 

        for index, (_type, time_stamp, company_id) in enumerate(receipts):

            if _type == 'A':

                points.append((time_stamp, index, company_id, True))

            else:

                points.append((time_stamp, index, company_id, False))

        points = sorted(points)

        results = [] 

        cur_A_index = -1 

        i = 0

        while i < len(points):

            if not points[i].is_type_A:

                i += 1 

                continue 

            else:

                cur_A_index = i 

                self.find_left_pair(cur_A_index, points, results, maxium_diff)
                self.find_right_pair(cur_A_index, points, results, maxium_diff)

                i += 1 

        return results


    # def next_A(self, curt_A_index, points):

    #     next_A_index = curt_A_index + 1 

    #     while next_A_index < len(points):

    #         if points[next_A_index].is_type_A:

    #             return next_A_index

    #     return -1 

            

    def find_left_pair(self, cur_A_index, points, results, maxium_diff):

        pos_B_index = cur_A_index -1 

        while pos_B_index >= 0:

            if points[pos_B_index].is_type_A:

                pos_B_index -= 1 
                
                continue 

            if not self.is_valid_timestamp_diff(points[pos_B_index][0], points[cur_A_index][0], maxium_diff):

                break 

            results.append((points[cur_A_index], points[pos_B_index]))

            pos_B_index -= 1 

    def find_right_pair(self, cur_A_index, points, results, maxium_diff):

        pos_B_index = cur_A_index + 1 

        while pos_B_index < len(points):

            if points[pos_B_index].is_type_A:

                pos_B_index += 1 
                
                continue 

            if not self.is_valid_timestamp_diff(points[pos_B_index][0], points[cur_A_index][0], maxium_diff):

                break 

            results.append((points[cur_A_index], points[pos_B_index]))

            pos_B_index += 1 

            

    def is_valid_timestamp_diff(self, tsp1, tsp2, maxium_diff):

        return abs(tsp1 - tsp2) <= maxium_diff



        

            