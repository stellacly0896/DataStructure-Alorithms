#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

def IsBinarySearchTree(root, min, max):
  if not root in tree:
    return True
  if tree[root][0] < min or tree[root][0] > max:
    return False
  return IsBinarySearchTree(tree[root][1], min, tree[root][0]-1) and IsBinarySearchTree(tree[root][2], tree[root][0], max)

def main():
  nodes = int(sys.stdin.readline().strip())
  global tree
  tree, int_max, int_min = {}, 4294967296, -4294967296
  for i in range(nodes):
    tree[i] = (list(map(int, sys.stdin.readline().strip().split())))
  if IsBinarySearchTree(0, int_min, int_max):
    print("CORRECT")
  else:
    print("INCORRECT")


threading.Thread(target=main).start()
