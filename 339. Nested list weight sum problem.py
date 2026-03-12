class Solution:
    def depthSum(self, nestedList):
        
        def dfs(nestedList, depth):
            total = 0
            
            for item in nestedList:
                if item.isInteger():
                    total += item.getInteger() * depth
                else:
                    total += dfs(item.getList(), depth + 1)
            
            return total
        
        return dfs(nestedList, 1)