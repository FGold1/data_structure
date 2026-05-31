class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def array_to_tree(arr):
    """将层序遍历数组（含 None）还原为二叉树链表结构"""
    if not arr or arr[0] is None:
        return None

    root = TreeNode(arr[0])
    queue = [root]
    i = 1
    while queue and i < len(arr):
        node = queue.pop(0)

        # 左子节点
        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1

        # 右子节点
        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1

    return root


def print_tree_visual(root):
    """打印美观的二叉树（精准对齐）"""
    if not root:
        return

    # 收集所有节点和位置
    levels = []
    queue = [(root, 0)]
    while queue:
        node, level = queue.pop(0)
        if len(levels) <= level:
            levels.append([])
        levels[level].append(node)
        if node:
            queue.append((node.left if node.left else None, level + 1))
            queue.append((node.right if node.right else None, level + 1))

    max_depth = len(levels) - 1

    # 计算树的宽度（每层的最大节点数）
    max_width = 2 ** (max_depth + 1)

    # 存储每个节点的显示位置
    pos = {}

    def dfs(node, x, y, width):
        if not node or y > max_depth:
            return
        pos[(x, y)] = str(node.val)
        if node.left:
            dfs(node.left, x - width // 2, y + 1, width // 2)
        if node.right:
            dfs(node.right, x + width // 2, y + 1, width // 2)

    # 初始位置：根节点在中间
    dfs(root, max_width // 2, 0, max_width // 2)

    # 构建树形输出
    result = []

    for y in range(max_depth + 1):
        # 当前层节点行
        node_line = [' '] * (max_width + 1)
        # 下一层的连线行
        line_line = [' '] * (max_width + 1)

        for (x, ly), val in pos.items():
            if ly == y:
                # 放置节点值
                for i, ch in enumerate(val):
                    node_line[x + i] = ch

                # 查找子节点并画连线
                for (cx, cly), cval in pos.items():
                    if cly == y + 1:
                        # 左子节点（在父节点左边）
                        if cx < x and abs(cx + len(cval) // 2 - x) < 5:
                            # 画左斜线
                            line_x = x - 1
                            if line_x >= 0:
                                line_line[line_x] = '/'
                        # 右子节点（在父节点右边）
                        elif cx > x and abs(cx + len(cval) // 2 - (x + len(val) - 1)) < 5:
                            # 画右斜线
                            line_x = x + len(val)
                            if line_x < len(line_line):
                                line_line[line_x] = '\\'

        # 去除尾部空格
        node_str = ''.join(node_line).rstrip()
        line_str = ''.join(line_line).rstrip()

        if node_str:
            result.append(node_str)
        if line_str and y < max_depth:
            result.append(line_str)

    # 输出
    for line in result:
        if line.strip():
            print(line)


# 给定数组
arr = [10, 5, 15, 3, 7, None, 20]

# 还原二叉树
root = array_to_tree(arr)

print("还原后的二叉树形态：")
print()
print_tree_visual(root)