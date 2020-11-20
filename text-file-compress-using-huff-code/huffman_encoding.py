from heapds import minHeap

result_dict = {}

class Node:
    def __init__(self, freq, char=None):
        self.freq = freq
        self.char = char
        self.code = None
        self.right = None
        self.left = None
    
    def __lt__(self, other):
        return self.freq < other.freq
    def __gt__(self, other):
        return self.freq > other.freq
    def __str__(self):
        return self.char+':'+str(self.freq)


def huffmanEncoding(input):
    heap = minHeap()
    
    for char in input.keys():
        heap.insert(Node(input[char], char))
    
    while heap.size() > 1:

        # pop 2 min-elements from heap
        n1 = heap.delete_min()
        n2 = heap.delete_min()
        
        # create a node and (f1+f2) and insert back
        inter_node = Node(int(n1.freq+n2.freq), 'non_leaf')
        inter_node.left = n1; inter_node.right = n2

        heap.insert(inter_node)
    
    huff_tree = heap.delete_min()
    return huff_tree


def assign_codes_preod(node, code):
    node.char = code
    if node.left != None:
        assign_codes_preod(node.left, code+'0')
    if node.right != None:
        assign_codes_preod(node.right, code+'1')
    if node.left == None and node.right == None:
        result_dict[node.char] = code

def get_codes(char_freq_dict):
    huff_tree = huffmanEncoding(char_freq_dict)
    assign_codes_preod(huff_tree, '')

    total_words = 0
    for char in char_freq_dict.keys():
        total_words += char_freq_dict[char]
    check = total_words == huff_tree.freq
    return check, result_dict, huff_tree


# test cases
# if __name__ == '__main__':
#     # input: char_frequencies
#     char_freq_dict = {'a': 13, 'b': 4, 'c': 11, 'd':3, 'e':22, 'f':14, 'g': 19, 'h':1, '?': 1}
#     huff_tree = huffmanEncoding(char_freq_dict)
#     assign_codes_preod(huff_tree, '')
#     print(result_dict, len(result_dict))
#     total_words = 0
#     for char in char_freq_dict.keys():
#         total_words += char_freq_dict[char]
#     print(total_words, huff_tree.freq)

    