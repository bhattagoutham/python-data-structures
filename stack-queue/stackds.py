# Stack and Queue data structure

# Two types of Stacks can be created => 1. Dynamic (No limit on size) 2. Fixed
# For imp. details check out the test-cases at the EOF.
# Stack opns => push, pop, top, size, isEmpty, isFull, get_min (O(n) space), print(stack)

# Queue

# Author : Goutham Bhatta

class Stack:
    def __init__(self, max_size, fixed=False):
        self.fixed = fixed
        if self.fixed:
            self.max_size = max_size            
        
        self.sz = 0
        self.stk = []
        self.min_stk = []

    def print_min_stack(self):
        return '['+'['.join([str(i) for i in self.min_stk])

    def __str__(self):
        return '['.join([str(i) for i in self.stk])

    def isEmpty(self):
        if self.sz > 0:
            return False
        return True
    
    def isFull(self):
        if self.fixed and self.sz >= self.max_size:
            return True
        return False

# make top and size as @property
    def top(self):
        if not self.isEmpty():
            return self.stk[-1]

    def size(self):
        return self.sz

    def push(self, e):
        if self.isFull():
            print("Stack is Full")
        else:
            self.stk.append(e)
            self.sz +=1

            # min_stk_code
            if self.sz == 1:
                self.min_stk.append(e)
            elif e <= self.min_stk[-1]:
                self.min_stk.append(e)

    def pop(self):
        if self.isEmpty():
            print("Stack is Empty")
            return None
        else:
            temp = self.stk[-1]
            del self.stk[-1]; self.sz-=1
            
            # min_stk_code
            if temp == self.min_stk[-1]:
                del self.min_stk[-1]

            return temp
    
    def get_min(self):
        # returns the min element in the entire stack.
        # if min_ele is popped then, returns the next min element.
        # takes -> O(n) space
        return self.min_stk[-1]
    


    
    
    # expandable stack check
    # stk = Stack(max_size=None, fixed = False)
    # for i in range(15):
        # stk.push((i, i))

    # print(stk)
    # print(stk.size(), stk.top()) # 15 14
    
    # # ovf, unf check
    # stk = Stack(max_size=5, fixed = True)
    # for i in range(6):
    #     stk.push(i)

    # for i in range(6):
    #     stk.pop()

    # # min stack test case
    # stk = Stack(max_size=None, fixed = False)
    # for i in [4, 5, 8, 3, 7, 13, 2, 11, 1]:
    #     stk.push(i)
    
    # print(stk.print_min_stack())
    # for i in range(9):
    #     stk.pop()
    #     print(stk.print_min_stack())
    
    
    
