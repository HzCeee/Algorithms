class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        for element in path.split("/"):
            if element == ".":
                pass
            elif element == "..":
                if stack: stack.pop()
            elif element != "":
                stack.append(element)
        
        ans = "/".join(stack)
        
        while ans and ans[-1] == "/":
            ans = ans[:-1]
            
        return "/" + ans if ans else "/"