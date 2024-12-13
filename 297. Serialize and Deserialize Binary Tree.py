# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    """
    Use . to split nodes 
    1.2.N.N.3.4.N.N.5.N.N
    serialize from tree to string(traverse tree)
    deserialize from string to tree(build tree)
    """
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        def preorder(node):
            if not node: 
                res.append("N")
                return
            res.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
        preorder(root)

        return ".".join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        ls = data.split(".")
        idx = 0
        def preorder():
            nonlocal idx
            if ls[idx] == "N":
                idx += 1
                return None
            # create node
            node = TreeNode(int(ls[idx]))
            idx += 1
            # build left and right subtree
            node.left = preorder()
            node.right = preorder()
            return node
        return preorder()





        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))