import math
f = open('input.txt', 'r')
lines = f.read().strip().split('\n')

def printTree(tree):
    if tree.value != None:
        return str(tree.value)
    s1 = printTree(tree.left)
    s2 = printTree(tree.right)
    return '[' + s1 + ',' + s2 + ']'


class Node:
    def __init__(self):
        self.left = None
        self.right = None

        self.depth = None
        self.parent = None

        self.value = None
        self.index = None

def findRightOf(node):
    while True:
        if node == None or node.parent == None:
            return None
        if node == node.parent.left:
            node = node.parent.right
            break
        node = node.parent
    while node.value == None:
        node = node.left
    return node

def findLeftOf(node):
    while True:
        if node == None or node.parent == None:
            return None
        if node == node.parent.right:
            node = node.parent.left
            break
        node = node.parent
    while node.value == None:
        node = node.right
    return node

def fromArray(array, d, p, i):
    r = Node()
    r.depth = d
    r.parent = p
    r.index = i
    if type(array) == int:
        r.value = array
        return r
    r.left = fromArray(array[0], d+1, r, 0)
    r.right = fromArray(array[1], d+1, r, 1)
    return r

def explode(tree):
    if tree.value != None:
        return False
    if tree.depth == 4:
        left = findLeftOf(tree)
        if left:
            left.value = left.value + tree.left.value
        right = findRightOf(tree)
        if right:
            right.value = right.value + tree.right.value
        n = Node()
        n.value = 0
        n.parent = tree.parent
        n.depth = tree.depth
        n.index = tree.index
        if tree.index == 0:
            tree.parent.left = n
        else:
            tree.parent.right = n
        return True
    v1 = explode(tree.left)
    if v1:
        return v1
    v2 = explode(tree.right)
    return v2

def split(tree):
    if tree.value == None:
        v1 = split(tree.left)
        if v1:
            return v1
        v2 = split(tree.right)
        if v2:
            return v2
        return False
    if tree.value < 10:
        return False

    half = tree.value / 2.0

    ln = Node()
    ln.depth = tree.depth + 1
    ln.value = int(math.floor(half))
    ln.index = 0
    ln.parent = tree

    rn = Node()
    rn.depth = tree.depth + 1
    rn.value = int(math.ceil(half))
    rn.index = 1
    rn.parent = tree

    tree.value = None
    tree.left = ln
    tree.right = rn

    return True

def addDepth(tree):
    if tree == None:
        return
    tree.depth += 1
    addDepth(tree.left)
    addDepth(tree.right)

def settle(root):
    counter = 0
    while True:
        exploded = explode(root)
        if exploded:
            counter += 1
            continue
        splitted = split(root)
        if splitted:
            continue
        break

def score(tree):
    if tree.value != None:
        return tree.value
    left = score(tree.left)
    right = score(tree.right)
    return 3 * left + 2 * right

def addition(tree, array):
    addDepth(tree)

    rt = fromArray(array, 0, None, None)
    addDepth(rt)

    root = Node()
    root.depth = 0
    root.left = tree
    root.right = rt

    rt.parent = root
    tree.parent = root

    return root

def magnitudeAdd(array1, array2):
    root = fromArray(array1, 0, None, None)
    settle(root)
    root = addition(root, array2)
    arr = eval(printTree(root))
    root = fromArray(arr, 0, None, None)
    settle(root)
    return score(root)

''' part 1
array = eval(lines[0])
root = fromArray(array, 0, None, None)
settle(root)
for line in lines[1:]:
    array = eval(printTree(addition(root, eval(line))))
    root = fromArray(array, 0, None, None)
    settle(root)
    print printTree(root)
'''
maxi = 0
for i in xrange(len(lines)):
    for j in xrange(len(lines)):
        if i == j:
            continue
        a1 = eval(lines[i])
        a2 = eval(lines[j])
        maxi = max(maxi,magnitudeAdd(a1, a2)) 
        maxi = max(maxi,magnitudeAdd(a2, a1)) 

print maxi
