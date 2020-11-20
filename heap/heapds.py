# min/max access => O(1)
# insert/delete => O(logn)
# priority_Q

class minHeap:
    def __init__(self):
        self.min_heap = []

    def swap(self, idx1, idx2):
        temp = self.min_heap[idx1]
        self.min_heap[idx1] = self.min_heap[idx2]
        self.min_heap[idx2] = temp

    # used for insert (i.e; heapify_up)
    def heapify_up(self, curr_idx):

        # if only one element in heap
        if curr_idx == 0:
            return
        
        parent_idx = int((curr_idx-1)/2)
        if parent_idx < 0 or self.min_heap[parent_idx] < self.min_heap[curr_idx]:
            return
        self.swap(parent_idx, curr_idx)
        self.heapify_up(parent_idx)
        # tail recursion

    # used for delete (i.e; heapify_down)
    def heapify_down(self, curr_idx):
        heap_sz = len(self.min_heap)
        left_c = self.min_heap[2*(curr_idx)+1] if 2*(curr_idx)+1 < heap_sz else None
        right_c = self.min_heap[2*(curr_idx)+2] if 2*(curr_idx)+2 < heap_sz else None
        
        
        # find min_child
        if left_c != None and right_c != None:
            min_child = min(left_c, right_c)
        elif left_c != None:
            min_child = left_c
        else:
            min_child = right_c
        
        # find min_idx
        if left_c != None and left_c == min_child:
            min_idx = 2*(curr_idx)+1
        elif right_c != None:
            min_idx = 2*(curr_idx)+2
        
        # node not in correct place
        if min_child != None and self.min_heap[curr_idx] > min_child:
            self.swap(curr_idx, min_idx)
            self.heapify_down(min_idx)

    def insert(self, e):
        self.min_heap.append(e)
        self.heapify_up(len(self.min_heap) - 1)

    def get_min(self):
        if len(self.min_heap) > 0:
            return self.min_heap[0]
    
    def delete_min(self):

        if len(self.min_heap) == 0:
            print('Heap Empty !')
            return

        temp = self.min_heap[0]
        self.min_heap[0] = self.min_heap[-1]
        del self.min_heap[-1]

        if len(self.min_heap) > 0:    
            self.heapify_down(0)
        
        return temp

    def size(self):
        return len(self.min_heap)

# test cases
if __name__ == '__main__':
    h = minHeap()
    for i in [3, 2, 4, 5, 6, 1, 6, 9, 8, 0]:
        h.insert(i)
    for i in range(11):
        print(h.get_min())
        h.delete_min()




    
