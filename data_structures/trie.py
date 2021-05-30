
class Node:
    """Node for use in Trie implementation.
    
    Args:
        is_complete (bool): whether this node is the end of it's complete chain.
    """
    def __init__(self, is_complete=False):
        self.children = {}
        self.is_complete = is_complete

    def add_child(self, id, node):
        """Add a child to this node.
        
        Args:
            id (str): id to add child node with.
            node (Node): node to add as child.
        Returns:
            bool: whether child was added succesfully.
        """
        if id not in self.children:
            self.children[id] = node
            return True

    def remove_child(self, id):
        """Remove child with given id from this node.

        Args:
            id (str): id of the child node to remove from this node.
        Returns:
            bool: whether child was removed succesfully.
        """
        if id in self.children:
            self.children.pop(id)
            return True


class Trie:
    """Trie data structure implementation."""
    def __init__(self):
        self.head = Node()

    def add_entry(self, id, is_complete=False, parent_node=None):
        """Add an entry to the trie.
        
        Args:
            id (str): id to add entry for.
            is_complete (bool): whether this entry is a valid complete point
                for it's chain.
            parent_node (Node): node to parent the entry under.
        Returns:
            Node: created node for the id.
        """
        if parent_node:
            if not isinstance(parent_node, Node):
                return
        else:
            parent_node = self.head
        node = Node(is_complete)
        parent_node.add_child(id, node)
        return node

    def add_chain(self, chain):
        """"Add a chain of nodes to the Trie.

        Args:
            chain (list): list of id's to add as a complete chain.
        """
        parent_node = self.head
        for id in chain:
            next_node = parent_node.children.get(id)
            if not next_node:
                next_node = Node()
                parent_node.add_child(id, next_node)
            parent_node = next_node
        parent_node.is_complete = True
        
    def is_valid_chain(self, chain):
        """Check whether given chain is a valid complete chain in the Trie.
        
        Args:
            chain (list): list of id's to add as a complete chain.
        Returns:
            bool: whether the chain is a complete chain in the Trie.
        """
        current_node = self.head
        for id in chain:
            current_node = current_node.children.get(id)
            if not current_node:
                return False
        return current_node.is_complete


def main():
    """Example usage."""
    contacts = Trie()
    contacts.add_chain('Anthony')
    contacts.add_chain('Tom')
    contacts.add_chain('Tony')

    assert(not contacts.is_valid_chain('To'))
    assert(contacts.is_valid_chain('Tom'))
    assert(not contacts.is_valid_chain('Tommy'))
    assert(contacts.is_valid_chain('Tony'))
