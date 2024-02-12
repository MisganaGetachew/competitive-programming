class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        l1 = {}
        l2 = {}
        com = []
        m  = 0
        for index, value in enumerate(list1):
            l1[value] = index    
        for index, value in enumerate(list2):         
            l2[value] = index
            
        # l1.sort(key = lambda  x: x[1])
        # l2.sort(key = lambda  x: x[1])
        
        for key, index in l1.items():
            if key in l2:
                # m += l2[key] + value
                com.append([key, index + l2[key] ])
                
        # s = float('inf')

        com.sort(key = lambda x: x[1])
        m = 0
        # return ["".join(com[0][0])]
        c = com[0][1]
        final = []
        for val, s in com:
            if s == c:
                final.append(val)
        return final
                
            
    
    
            
                
            
    


        