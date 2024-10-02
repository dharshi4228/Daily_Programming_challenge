class Node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
    @staticmethod
    def insertLevelOrder(arr,root,i,n ):
        if i<n:
            temp=Node(arr[i])
            root=temp
            root.left=Node.insertLevelOrder(arr,root.left,2*i+1,n)
            root.right=Node.insertLevelOrder(arr,root.right,2*i+1,n)
        return root
        
    @staticmethod      
    def findLCA(root,n1,n2):
        if root is None:
            return None
        if root.key==n1 or root.key==n2:
            return root
            
        left_lca = Node.findLCA(root.left,n1,n2)
        right_lca=Node.findLCA(root.right,n1,n2)
        
        if left_lca and right_lca:
            return root
        return left_lca if left_lca is not None else right_lca
        
if __name__=="__main__":
    inp=input("Enter the binary tree nodes")
    arr=inp.split(',')
    
    arr=[int(x) if x.strip() != 'null' else None for x in arr]
    root=None
    root= Node.insertLevelOrder(arr,root,0,len(arr))
    
    p=int(input("enter the first node(p) "))
    q=int(input("enter the second node"))
    lca = Node.findLCA (root,p,q)
    if lca:
        print(f"LCA({p},{q})=",lca.key)
    else:
        print(f"LCA{p}, {q} ) not found")
        