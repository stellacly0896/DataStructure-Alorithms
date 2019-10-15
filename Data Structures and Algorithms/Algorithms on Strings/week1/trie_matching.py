# python3
import sys

"""
NA = -1

class Node:
	def __init__ (self):
		self.next = [NA] * 4
"""


def build_trie(patterns):
    tree = dict()
    tree[0] = dict()
    node = 1 #root has to be empty
    
    for pattern in patterns:
        current_node = 0
        for symbol in pattern:
            if symbol in tree[current_node]:
                current_node = tree[current_node][symbol]
            else:
                tree[current_node][symbol] = node
                tree[node] = dict()
                current_node = node
                node += 1    
    return tree

def match(text,trie):
    i = 0
    symbol = text[i]
    current = trie[0]
    
    while True:
        if symbol in current:
            if current[symbol] not in trie or not any(trie[current[symbol]]):
                return True
            elif i != len(text) - 1:
                current = trie[current[symbol]]
                i += 1
                symbol = text[i]
            else:
                return False
        else:
            return False
            
def solve (text, n, patterns):

    result = []
    trie = build_trie(patterns)
    
    for i in range(len(text)):
        if match(text[i:],trie):
            result.append(i)
            
    return result



text = sys.stdin.readline ().strip ()
n = int (sys.stdin.readline ().strip ())
patterns = []
for i in range (n):
	patterns += [sys.stdin.readline ().strip ()]

ans = solve (text, n, patterns)

sys.stdout.write (' '.join (map (str, ans)) + '\n')
