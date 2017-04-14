class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild is not None

    def hasRightChild(self):
        return self.rightChild is not None

    def isLeftChild(self):
        return self.parent and self.parent.leftChild is self

    def isRightChild(self):
        return self.parent and self.parent.rightChild is self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return not self.isLeaf()

    def hasBothChildren(self):
        return self.hasLeftChild() and self.hasRightChild()

    def replaceNodeData(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

    def findSuccessor(self):
        #               20
        #             /    \
        #   (self)-> 9      24
        #         /    \
        #        6      18
        #      /  \     /  \
        #     4    7   15   19
        #             /  \
        #           14    16
        #          /
        #         11 <--- successor : the next largest key.
        #           \
        #            12
        # >>> 1) Go to right child. 2) Go to last left child.
        succ = None
        if self.isLeaf():
            return None
        if self.hasRightChild():
            return self.rightChild.findMin()
        # If no right child, its parent is successor
        # But in a binary search tree, there is no case like this because
        # the successor is needed when the node to be removed has both child
        # nodes.
        if self.parent and self.isLeftChild():
            return self.parent

    def findMin(self):
        if self.hasLeftChild():
            return self.leftChild.findMin()
        else:
            return self

    def sliceOut(self):
        """ move node's child to its own position """
        if self.parent and self.hasRightChild():
            if self.isLeftChild():
                self.parent.leftChild = self.rightChild
            else:
                self.parent.rightChild = self.rightChild
                # !!! the successor node never has a left child.

    def traverse(self):
        # ! in-order traverse prints out an sotred list.
        if self.hasLeftChild():
            self.leftChild.traverse()
        print(self.payload)
        if self.hasRightChild():
            self.rightChild.traverse()


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size += 1

    def _put(self, key, val, currentNode):
        if key < currentNode.key:
            #         currentnode
            #        /
            #    new-child?
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            # currentnode
            #         /
            #      leftchild
            #        |
            #    new-child?
            else:
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
        else:
            #         currentnode
            #                   \
            #                    new-child?
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            # currentnode
            #                   \
            #                 rightchild
            #                     |
            #                  new-child?
            else:
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)

    def __setitem__(self, k, v):
        self.put(k, v)

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        return None

    def _get(self, key, currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            #
            #                root node
            #                /        \
            #           smaller key   greater key
            #          /                  \
            #        left child            right child
            #  --------------------------------------------
            return currentNode
        elif key < currentNode.key:
            return self._get(key, currentNode.leftChild)
        else:
            return self._get(key, currentNode.rightChild)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False

    def delete(self, key):
        if self.size > 1:
            nodeToRemove = self._get(key, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size -= 1
            else:
                raise KeyError('Error, key is not in tree')

        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = 0

        else:
            raise KeyError('Error, key not in tree')

    def __delitem__(self, key):
        self.delete(key)

    def remove(self, currentNode):
        if currentNode.isLeaf():
            if currentNode.isLeftChild():
                # current node is left child of its parent node.
                #                parent
                #              /
                #          currentNode << DELETE
                currentNode.parent.leftChild = None
            else:
                # current node is left child of its parent node.
                #                parent
                #                       \
                #                       currentNode <<< REMOVE
                currentNode.parent.rightChild = None
        elif currentNode.hasBothChildren():
            #          parent
            #            |
            #        current node << REMOVE
            #       /            \
            #  left-child     right-child
            # ---------------------------------------------------------
            # REPLACE CURRENT NODE with NEXT LARGEST NODE (only key and payload)
            #
            #        current node << REMOVE
            #       /            \
            #  left-child     right-child << NEXT?
            #                /
            #           next-left-child
            #          /
            #   next-next-left-child  <<< NEXT!!! = (SUCCESSOR)
            #                     \
            #                       Successor's rightChild
            # ---------------------------------------------------------
            # Successor's right child move to its parent's position.
            # This is done with 'node.sliceOut()'
            #
            #         (SUCCESSOR)
            #       /            \
            #  left-child     right-child << NEXT?
            #                /
            #           next-left-child
            #          /
            #        Successor's right child
            succ = currentNode.findSuccessor()
            succ.sliceOut()
            currentNode.key = succ.key
            currentNode.payload = succ.payload


        elif currentNode.hasLeftChild():
            if currentNode.isLeftChild():
                # current node is left child of its parent node.
                #                parent
                #              /
                #          currentnode << remove
                #         /
                #   childnode
                currentNode.parent.leftChild = currentNode.leftChild
            else:
                # current node is left child of its parent node.
                #                parent
                #              /
                #          currentNode <<< REMOVE
                #                      \
                #                       childnode
                currentNode.parent.rightChild = currentNode.leftChild
        else:
            if currentNode.isLeftChild():
                # current node is left child of its parent node.
                #            parent
                #          /
                #      currentNode <<< REMOVE
                #                 \
                #                  childnode
                currentNode.parent.rightChild = currentNode.rightChild
            else:
                # current node is right child of its parent node.
                #       parent
                #             \
                #             currentNode <<< REMOVE
                #                        \
                #                        childnode
                currentNode.parent.rightChild = currentNode.leftChild


def main():
    b = BinarySearchTree()
    ad = (17, 5, 25, 2, 11, 29, 38, 9, 16, 7, 8)
    for i in ad:
        b.put(i, i)
    b.root.traverse()
    print('remove 5')
    b.delete(5)
    b.root.traverse()


if __name__ == "__main__":
    main()