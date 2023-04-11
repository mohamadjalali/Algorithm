
a = [1, 3, 5, 7, 9]
b = [2, 4, 6, 8, 10]


class ZigZag:

    def __init__(self, l1, l2):
        self.queue = [l1, l2]

    
    def next(self):
        v = self.queue.pop(0)
        r = v.pop(0)
        if v:
            self.queue.append(v)
        return r

    
    def has_next(self):
        if self.queue:
            return True
        else:
            return False

    
#z = ZigZag(a, b)

#while z.has_next():
#    print(z.next(), end=' ')

