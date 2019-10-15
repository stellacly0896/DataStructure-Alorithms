# python3

import sys
import threading

class TreeHeight:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))

    def compute_height(self):
        # Replace this code with a faster implementation
        max_height = 0
        heights = [0] * len(self.parent)
        for vertex in range(self.n):
            if (heights[vertex] != 0):
                continue
            height = 0
            i = vertex
            while i != -1:
                if (heights[i] != 0):
                    height += heights[i]
                    break
                height += 1
                i = self.parent[i]
            max_height = max(max_height, height)
            i = vertex
            while i != -1:
                if (heights[i] != 0):
                    break
                heights[i] = height
                height -= 1
                i = self.parent[i]
        return max_height


def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height())


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
