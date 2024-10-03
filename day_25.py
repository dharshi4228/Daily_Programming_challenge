class Node:
    def __init__(self,value):
        self.data=value
        self.left=None
        self.right=None
        
def isBST(node,min_value,max_value):
    if node is None:
        return True
            
    if node.data<=min_value or node.data >=max_value:
        return False
    return (isBST(node.left,min_value,node.data)and
    isBST(node.right,node.data,max_value))
        
def isBst(node):
    return isBST(node,float('-inf'),float('inf'))
        
if __name__=="__main__":
    root=Node(4)
    root.left=Node(2)
    root.right =Node(5)
    root.left.left=Node(1)
    root.left.right=Node(3)

    if isBst(root):
        print("True")
    else:
        print("False")