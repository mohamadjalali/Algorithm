
a = [1, 3, 5, 7, 9]
b = [2, 4, 6, 8, 10]


class ZigZag:

    def __init__(self, l1, l2):
        self.queue = [l1, l2]


    def next_1(self):
        v = self.queue.pop(0)
        r = v.pop(0)
        if v:
            self.queue.append(v)
        return r

 
    def next(self):
        if not self.queue:
            return None
        v = self.queue.pop(0)
        if v:
            r = v.pop(0)
            self.queue.append(v)
            if r:
                return r
        return self.next()

    
    def has_next(self):
        if self.queue:
            return True
        else:
            return False

    
if __name__ == "__main__":
    z = ZigZag(a, b)
    result = ''
    while z.has_next():
        print(z.next(), end=' ')
