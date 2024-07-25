
from typing import List

class Node:
    def __init__(self, char: str, freq: int):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq

class Solution:
    def huffmanCodes(self, S: str, f: List[int], N: int) -> List[str]:
        # Edge case: if the length of S and f are not equal
        if len(S) != N or len(f) != N:
            raise ValueError("Length of S and f must be equal to N.")
        
        # Step 1: Create a list of nodes
        nodes = [Node(char, freq) for char, freq in zip(S, f)]
        
        # Step 2: Build the Huffman Tree
        while len(nodes) > 1:
            # Sort nodes by frequency
            nodes.sort()
            
            # Pick two nodes with the smallest frequency
            left = nodes.pop(0)
            right = nodes.pop(0)
            
            # Create a new internal node with these two nodes as children
            merged = Node(None, left.freq + right.freq)
            merged.left = left
            merged.right = right
            
            # Add the new node to the list
            nodes.append(merged)
        
        # The last remaining node is the root of the Huffman Tree
        root = nodes[0]
        
        # Step 3: Generate Huffman codes
        def generate_codes(node, code, codes):
            if node is not None:
                if node.char is not None:
                    codes[node.char] = code
                generate_codes(node.left, code + "0", codes)
                generate_codes(node.right, code + "1", codes)
        
        codes = {}
        generate_codes(root, "", codes)
        
        # Step 4: Map characters to their Huffman codes
        result = [codes[char] for char in S]
        return result