class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSymmetric(root: TreeNode) -> bool:
    if not root:
        return True
    
    def isMirror(left: TreeNode, right: TreeNode) -> bool:
        
        if not left and not right:
            return True
        if not left or not right:
            return False
        
       
        return (left.val == right.val) and isMirror(left.left, right.right) and isMirror(left.right, right.left)
    
  
    return isMirror(root.left, root.right)

if __name__ == "__main__":
    tree1 = TreeNode(1, 
                     TreeNode(2, TreeNode(3), TreeNode(4)), 
                     TreeNode(2, TreeNode(4), TreeNode(3)))
    print(isSymmetric(tree1))  


    tree2 = TreeNode(1, 
                     TreeNode(2, None, TreeNode(3)), 
                     TreeNode(2, None, TreeNode(3)))
    print(isSymmetric(tree2)) 

    
    tree3 = TreeNode(1)
    print(isSymmetric(tree3))

   
    tree4 = None
    print(isSymmetric(tree4)) 

    tree5 = TreeNode(1, 
                     TreeNode(2, TreeNode(3)), 
                     TreeNode(2, None, TreeNode(3)))
    print(isSymmetric(tree5))