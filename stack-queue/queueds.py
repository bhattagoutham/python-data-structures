class Q:
    def __init__(self):
        self.q = []
    
    def __str__(self):
        return ']'.join([str(i) for i in self.q])+']'
    
    def isEmpty(self):
        if len(self.q):
            return False
        return True
        
    def push(self, e):
        # push multiple elemets at once
        if type(e) is list:
            for i in e:
                self.q.append(e)
        else:
            self.q.append(e)
    
    def pop(self):
        if len(self.q):
            temp = self.q[0]
            del self.q[0]
            return temp
        print('Q is Empty')

    def top(self):
        return self.q[0]

# test_cases
if __name__ == '__main__':
    # Q check

    q = Q()
    for i in range(7):
        q.push(i)
    for i in range(3):
        print(q.pop())
    print(q)
