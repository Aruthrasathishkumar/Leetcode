def binaryTreePaths(root):
    def dfs(node, path, paths):
        if not node:
            return

        path += str(node.val)

        if not node.left and not node.right:
            paths.append(path)
        else:
            path += '->'
            dfs(node.left, path, paths)
            dfs(node.right, path, paths)

    paths = []
    dfs(root, '', paths)
    return paths