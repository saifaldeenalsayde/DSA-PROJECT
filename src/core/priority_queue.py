class MinPQ:
    def __init__(self, initial_capacity=1):
        self.capacity = initial_capacity + 1
        self.pq = [None] * self.capacity
        self.n = 0

    def is_empty(self):
        return self.n == 0

    def size(self):
        return self.n
    
    def min(self):
        if self.is_empty():
            raise IndexError("Priority queue underflow")
        return self.pq[1]

    def insert(self, key):
        if self.n == self.capacity - 1:
            self.resize(2 * self.capacity)
        self.n += 1
        self.pq[self.n] = key
        self.swim(self.n)

    def del_min(self):
        if self.is_empty():
            raise IndexError("Priority queue underflow")
        min_key = self.pq[1]
        self.exch(1, self.n)
        self.n -= 1
        self.sink(1)
        self.pq[self.n + 1] = None  
        if self.n > 0 and self.n == (self.capacity - 1) // 4:
            self.resize(self.capacity // 2)
        return min_key

    def swim(self, k):
        while k > 1 and self.greater(k // 2, k):
            self.exch(k, k // 2)
            k = k // 2

    def sink(self, k):
        while 2 * k <= self.n:
            j = 2 * k
            if j < self.n and self.greater(j, j + 1):
                j += 1
            if not self.greater(k, j):
                break
            self.exch(k, j)
            k = j

    def greater(self, i, j):
        return self.pq[i] > self.pq[j]

    def exch(self, i, j):
        temp = self.pq[i]
        self.pq[i] = self.pq[j]
        self.pq[j] = temp

    def resize(self, new_capacity):
        temp = [None] * new_capacity
        i = 1
        while i <= self.n:
            temp[i] = self.pq[i]
            i += 1
        self.pq = temp
        self.capacity = new_capacity