class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        simplified

        . -> current directory
        .. -> prev/parent directory
        //, /// -> /

        ... or .... => file name-> using

        """
        stack = []
        curr = ""

        for ch in path + "/": # add / at the end to finish the last curr
            if ch == "/":
                if curr == "..":
                    if stack:
                        stack.pop()
                elif curr != "" and curr != ".":
                    stack.append(curr)
                curr = ""
            else:
                curr += ch
        
        return "/" + "/".join(stack)