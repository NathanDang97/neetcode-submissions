class Solution:
    def simplifyPath(self, path: str) -> str:
        directory_stack = []
        path = path.split("/")

        for s in path:
            if directory_stack and s == "..":
                directory_stack.pop()
            elif s not in ["", ".", ".."]:
                directory_stack.append(s)

        return '/' + '/'.join(directory_stack)