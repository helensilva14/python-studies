#!/bin/python3

import os
import sys

class Node:
    def __init__(self):
        self.count = 1
        self.children = dict()

def add(node, name):
    for letter in name:
        child = node.children.get(letter)  
        if child:
            child.count += 1
        else:
            child = node.children[letter] = Node()  
        node = child  

def find(node, search):
    for letter in search:
        child = node.children.get(letter)  
        if not child:
            return 0
        node = child
    return node.count  

#
# Complete the contacts function below.
#
def contacts(queries):
    root = Node()
    result = list()
    for query in queries:
        if query[0] == 'add': 
            add(root, query[1])
        if query[0] == 'find':
            result.append(find(root, query[1]))
        
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    queries_rows = int(input())

    queries = []

    for _ in range(queries_rows):
        queries.append(input().rstrip().split())

    result = contacts(queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
