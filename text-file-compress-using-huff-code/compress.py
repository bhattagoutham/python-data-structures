# Author : Goutham Bhatta


import sys
import huffman_encoding as huff_enc

# Compress a text file using huffman encoding
class Compress:

    def __init__(self, fname):
        self.fname = fname
        self.char_freq_dict = {}
        self.huff_code_str = None
        self.huff_codes = None
        self.huff_tree = None
        
    # reads the text file and creates a {char:freq} dict
    def read_file(self):

        with open(self.fname, 'r') as fp:
            while True:
                char = fp.read(1)
                if not char:
                    break
                
                if char in self.char_freq_dict:
                    self.char_freq_dict[char] += 1
                else:
                    self.char_freq_dict[char] = 1

    #  converts file contents to a huff coded binary string
    def encode_to_str(self, huff_codes):
        
        with open(self.self.fname+'.txt', 'r') as fp:
            while True:
                char = fp.read(1)
                if not char:
                    break
                self.huff_code_str += huff_codes[char]


    # writes the huff coded string to a binary file
    # Note: since 1 byte is consumed for each char, 
    # we convert binary string to its corresponding raw byte form
    # str(0,1)[8-bits] => int => to_bytes()
    def write_to_file(self):
        
        fname_without_ext = self.fname[0:self.fname.find('.')]

        with open(fname_without_ext +'.bin', 'wb') as fw:
            i = 0; nof_bytes = 0
            n = len(huff_code_str)
            fw.write(n.to_bytes(4, 'big'))
            while i < n:
                start = i
                end = n if i+8 > n else i+8
                byte_str = huff_code_str[start:end]
                byte = int(byte_str, base=2).to_bytes(1, 'big')
                fw.write(byte)
                i = end; nof_bytes += 1
                
            print('encoded:', nof_bytes)

            # saving huff_codes, for future use during decompress
            # self.fname_without_ext = [0:self.fname.find('.')]
            # with open(self.fname_without_ext+'_huff_tree.txt', 'w') as fw:
            #     fw.write(str(huff_codes))

    def preorder_traversal(self):
        result = ''
        root = self.huff_tree
        while not stk.isEmpty():
            while(root == None):
                root = root.left
                stk.push(root)
                result += root.char 
            if not stk.isEmpty():
                root = stk.pop().right

        return result

    def inorder_traversal(self):
        result = ''
        root = self.huff_tree
        while not stk.isEmpty():
            while(root == None):
                root = root.left
                stk.push(root)
                
            if not stk.isEmpty():
                root = stk.pop()
                result += root.char 
                root = root.right

        return result
            
            
    def save_huff_tree(self):
        # if built from char_codes take O(nof_bits)
        # if built from traversal takes O(n)
        pre = self.preorder_traversal()
        ino = self.inorder_traversal()

        print('pre: ', pre)
        print('In: ', ino)
        self.fname_without_ext = [0:self.fname.find('.')]
        with open(self.fname_without_ext+'_huff_tree.txt', 'w') as fw:
            fw.write(pre+'\n'+ino)


    # checks % of space saved
    def sanity_check(self, huff_codes):
        saved_bits = 0
        total_bits = 0
        for char in huff_codes.keys():
            saved_bits += (8 - len(huff_codes[char]))*self.char_freq_dict[char]
            total_bits += (self.char_freq_dict[char]*8)
        print('space saved: '+str(int((saved_bits/total_bits)*100))+'%' )

    def compress(self):
        self.read_file()
        freq_check, self.huff_codes, huff_tree = huff_enc.get_codes(self.char_freq_dict)
        # self.sanity_check()
        # self.encode_to_str()
        # self.write_to_file()

        # save huff_tree for decoding
        self.save_huff_tree()
        


class Decompress:
    
    # input is the binary file obtained during compress
    def __init__(self, fname):
        self.fname = fname
        self.huff_tree = None
        self.decoded_str = None

    # returns binary rep of the data
    def bytes_to_bits(self):
        decoded_str = ''

        with open(self.fname, 'rb') as fp:
            byte = fp.read(4)
            file_len = int.from_bytes(byte, 'big')
            flag = (0 if file_len%8 == 0 else 1)
            nof_bytes = file_len//8 + flag
            print('decoded:', nof_bytes)        
            
            while nof_bytes > 0:
                byte = fp.read(1)
                
                # binary format => '0b01001' => need to exclude '0b' part
                byte_str = str(bin(int.from_bytes(byte, 'big'))[2:])
                # binary format ignores msb zeros, hence explicitly added them
                if len(byte_str) < 8:
                    byte_str ='0'*(8-len(byte_str)) + byte_str
                
                # if nof_bits not a multiple of 8, 
                # then select only valid part of last byte
                if nof_bytes == 1 and flag == 1:
                    decoded_str += byte_str[-(len%8):]
                else:
                    decoded_str += byte_str
                nof_bytes -= 1
                
        self.decoded_str = decoded_str        

    def build_tree(self, preorder, inorder):
        pass

    def decode_huff_tree(self):
        ht_fname = self.fname[0:self.fname.find('.')]+'_huff_tree.txt'

        with open(ht_fname, 'r') as f:

            preorder = f.readline()
            inorder = f.readline()

        self.build_tree(preorder, inorder)

    def decode_str(self):
        i = 0
        curr_node = huff_tree
        result = ''
        while i < len(decoded_str):
            if curr_node.left == None and curr_node.right == None:
                result += curr_node.char
                curr_node = huff_tree
                continue
            elif decoded_str[i] == '0':
                curr_node = curr_node.left    
            else:
                curr_node = curr_node.right
            i += 1
            
        return result
    

if __name__ == '__main__':
    
    

    # decoded_str = decompress(self.fname+'.bin', huff_codes)
    # decode_str(huff_tree, decoded_str)
    
    
    
    
