class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # lets bubble sort the numbers while holding there original index with hashmap.
        # lets compare and rearrange the string position with the new order 
        from collections import defaultdict

        my_map = defaultdict(list)
        for i in range(len(names)):
            my_map[heights[i]].append(names[i])
        print(my_map)
        heights = list(set(heights))
        size = len(heights)
        for j in range(size):
            for k in range(size - j - 1):
                if heights[k] < heights[k + 1]:
                    heights[k], heights[k + 1] = heights[k + 1], heights[k]
        newlist = []
        for m in range(size):
            newlist.extend(my_map[heights[m]])
        
        return newlist


        