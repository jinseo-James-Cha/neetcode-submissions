class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  

# class TrieNode:
#     def __init__(self):
#         self.children = {}
#         self.is_word = False
    
#     def add(self, word):
#         curr = self
#         for ch in word:
#             if ch not in curr.children:
#                 curr.children[ch] = TrieNode()
#             curr = curr.children[ch]
#         curr.is_word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # True + DFS + Backtracking
        # 1. Trie 생성
        root = TrieNode()

        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = word

        rows, cols = len(board), len(board[0])
        ans = []

        DIRS = [(1,0), (-1,0), (0,1), (0,-1)]

        def dfs(r, c, node):

            ch = board[r][c]

            if ch not in node.children:
                return

            next_node = node.children[ch]

            if next_node.word:
                ans.append(next_node.word)
                next_node.word = None

            board[r][c] = "#"
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc

                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and board[nr][nc] != "#"
                ):
                    dfs(nr, nc, next_node)

            board[r][c] = ch

            if not next_node.children and next_node.word is None:
                del node.children[ch]

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return ans


        # Trie - hashmap
        root = TrieNode()
        for word in words:
            root.add(word)
        
        m,n = len(board), len(board[0])
        res = set()

        def is_within_bounds(row, col):
            return 0 <= row < len(board) and 0 <= col < len(board[0])

        DIRS = [(1,0), (-1,0), (0,1), (0,-1)]
        def dfs(row, col, node, word):
            if node.is_word:
                res.add(word)
            
            temp = board[row][col]
            board[row][col] = "#"
            
            for dy, dx in DIRS:
                next_r, next_c = row+dy, col+dx
                if is_within_bounds(next_r, next_c) and board[next_r][next_c] != "#" and board[next_r][next_c] in node.children:

                    next_node = node.children[board[next_r][next_c]]
                    dfs(next_r, next_c, next_node, word+board[next_r][next_c] )
            board[row][col] = temp

        for row in range(m):
            for col in range(n):
                if board[row][col] in root.children:
                    dfs(row, col, root.children[board[row][col]], board[row][col])
        
        return list(res)

        
        # DFS - TLE
        def is_within_bounds(row, col):
            return 0 <= row < len(board) and 0 <= col < len(board[0])

        DIRS = [(1,0), (-1,0), (0,1), (0,-1)]
        def dfs(idx, word, row, col, visited):
            if idx == len(word)-1:
                return True
            
            for dy, dx in DIRS:
                next_r, next_c = row+dy, col+dx
                if is_within_bounds(next_r, next_c) and (next_r, next_c) not in visited and word[idx+1] == board[next_r][next_c]:
                    visited.add((next_r, next_c))
                    if dfs(idx+1, word, next_r, next_c, visited):
                        return True
                    visited.remove((next_r, next_c))
            return False
        
        first_letter_maps = defaultdict(list)
        for word in words:
            first_letter_maps[word[0]].append(word)
        

        res = []
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] in first_letter_maps:
                    for word in first_letter_maps[board[row][col]]:
                        if dfs(0, word, row, col, {(row, col)}):
                            res.append(word)
        
        return res