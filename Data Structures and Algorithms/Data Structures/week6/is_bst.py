#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

def IsBinarySearchTree(tree):
    if not tree:
        return True
    stack = []
    pre = None
    while tree and stack:
        while tree:
            stack.append(tree)
            tree = tree.left
        tree = stack.pop()
        if pre and tree.val <= pre.val:
            return False
        pre = tree
        tree = tree.right
    return True


def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
