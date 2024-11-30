# Trie Node class for searching by name/address with partial matches
class TrieNode:
    def __init__(self):
        self.children = {}
        self.hospitals = []

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, key, hospital):
        """Insert a hospital into the Trie based on the key (name or address)."""
        node = self.root
        for char in key.lower():
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.hospitals.append(hospital)

    def search(self, partial_key):
        """Search for hospitals based on a partial key (name or address)."""
        node = self.root
        for char in partial_key.lower():
            if char not in node.children:
                return []  # No matches found
            node = node.children[char]
        return self._collect_all_hospitals(node)

    def _collect_all_hospitals(self, node):
        """Collect all hospitals from the current node and its children."""
        hospitals = list(node.hospitals)
        for child_node in node.children.values():
            hospitals.extend(self._collect_all_hospitals(child_node))
        return hospitals
