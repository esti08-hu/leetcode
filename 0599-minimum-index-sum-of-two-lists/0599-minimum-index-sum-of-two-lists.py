class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        min_i_sum = float("inf")
        min_s = [""]
        for i in list1:
            if i in list2:
                if(list1.index(i) + list2.index(i)) < min_i_sum:
                    min_i_sum = list1.index(i) + list2.index(i)
                    min_s[-1] = i
                elif (list1.index(i) + list2.index(i)) == min_i_sum:
                    min_s.append(i)
        return min_s

        