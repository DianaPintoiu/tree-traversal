from node import Node


class Tree:
    """ Tree class for binary tree """

    def __init__(self):
        """ Constructor for Tree class """
        self.root = None

    def getRoot(self):
        """ Method for get root of the tree """
        return self.root

    def add(self, data):
        """ Method for add data to the tree """
        if self.root is None:
            self.root = Node(data)
        else:
            self._add(data, self.root)

    def _add(self, data, node):
        """Method for add data to the tree

        Args:
            data (int): data to add

        Returns:
            None
        """
        if data < node.data:
            if node.left is not None:
                self._add(data, node.left)
            else:
                node.left = Node(data)
        else:
            if node.right is not None:
                self._add(data, node.right)
            else:
                node.right = Node(data)

    def find(self, data):
        """Method for find data in the tree

        Args:
            data (int): data to find

        Returns:
            Node: node with data
        """
        if self.root is not None:
            return self._find(data, self.root)
        else:
            return None

    def _find(self, data, node):
        if data == node.data:
            return node
        elif (data < node.data and node.left is not None):
            return self._find(data, node.left)
        elif (data > node.data and node.right is not None):
            return self._find(data, node.right)

    def deleteTree(self):
            """
            Deletes the entire tree by setting the root node to None.

            Parameters:
                None

            Returns:
                None
            """
            self.root = None

    def printTree(self):
            """
            Prints the elements of the tree in inorder traversal.

            Returns:
                None
            """
            if self.root is not None:
                self._printInorderTree(self.root)

    def _printInorderTree(self, node):
            """
            Prints the elements of the binary tree in inorder traversal.

            Parameters:
                node (TreeNode): The root node of the binary tree.

            Returns:
                None
            """
            if node is not None:
                self._printInorderTree(node.left)
                print(str(node.data) + ' ')
                self._printInorderTree(node.right)

    def _printPreorderTree(self, node):
        """
        Prints the nodes of the tree in preorder traversal.

        Parameters:
        - node: The current node being visited.

        Returns:
        - None
        """
        if node is not None:
            print(str(node.data) + ' ')
            self._printPreorderTree(node.left)
            self._printPreorderTree(node.right)
        

    def _printPostorderTree(self, node):
        """
        Prints the nodes of the tree in postorder traversal.

        Parameters:
        - node: The root node of the tree (or subtree) to be traversed.

        Returns:
        None
        """
        if node is not None:
            self._printPostorderTree(node.left)
            self._printPostorderTree(node.right)
            print(str(node.data) + ' ')


