class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        
        # Split the path by '/'
        parts = path.split('/')
        
        for token in parts:
            # Skip empty and current directory
            if token == "" or token == ".":
                continue
            
            # Go back to parent directory
            if token == "..":
                if stack:
                    stack.pop()
            else:
                # Valid directory name
                stack.append(token)
        
        # If stack is empty, return root
        if not stack:
            return "/"
        
        # Build the result path
        return "/" + "/".join(stack)

# Time complexity: O(N)
# Space complexity: 2 O(N)