class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''
def height(root):
    # print(type(root))
    if root == None: return -1
    if root.left == None and root.right == None:
        return 0
    return max(height(root.left), height(root.right)) + 1

def inOrder(root):
    if root is None: print('')
    # print the node value with spacing
    print(root, end = ' ')

    if root.left: 
        inOrder(root.left)
    if root.right:
        inOrder(root.right)  


  #=====================================================================
  # Author: Isai Damier
  # Title: Level Order Traversal
  # Project: geekviewpoint
  # Package: algorithms
  #
  # Time Complexity of Solution:
  #   Best = Average = Worst = O(n).
  #
  # Description: visit node; visit cousins; visit children and nephews.
  #   Level-order (aka breadth-first) traversal visits the elements of a
  #   binary search tree one level at a time. Imagine a BST as a family
  #   tree: with siblings and cousins and uncles, etc; level order, then,
  #   visits the nodes by generation. The grand-parent generation is
  #   visited first; then the parent generation; then the children
  #   generation.
  #
  # Technical Details: Of all the fundamental traversal techniques, level
  #   order is the only one that uses a queue. All the other techniques
  #   use a stack, because they are depth-first algorithms. In python
  #   a LifoQueue may be used to implement a stack.
  #
  # 0] preliminary checks:
  #     1) return if self.root is None
  #     2) create queue
  # 1] add the self.root to the queue
  # 2] while the queue is not empty
  #     1) dequeue a node from the queue
  #     2) visit the node
  #     3) add the children of the node to the queue if they are not None
  #
  # Application:
  #    print BST to file then read file back as same BST
  #
  #=====================================================================
def levelOrder(root):
    if root is None: return

    queue = []
    queue.append(root)

    while(len(queue) > 0): 
        # print the node value with spacing
        print(queue[0], end = ' ')
        node = queue.pop(0)

        if node.left: 
            queue.append(node.left)

        if node.right:
            queue.append(node.right)               

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

print(height(tree.root))