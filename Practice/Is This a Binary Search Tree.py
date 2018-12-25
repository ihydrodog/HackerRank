""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def _checkBST( node, left, right ):
    data = node.data

    if left < data < right:
        if node.left and _checkBST( node.left, left, data) == False:
            return False
        if node.right and _checkBST( node.right, data, right) == False:
            return False

        return True
    else:
        return False




def checkBST(root):
    MIN = -1
    MAX = 100000

    return _checkBST( root, MIN, MAX )