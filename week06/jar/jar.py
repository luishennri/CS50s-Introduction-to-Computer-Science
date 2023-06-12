class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError('Wrong capacity')
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return self.size * "🍪"

    def deposit(self, n):
        if n > self.capacity:
            raise ValueError('Exceed capacity')
        elif self.size + n > self.capacity:
            raise ValueError('Exceed capacity')
        else:
            self._size += n


    def withdraw(self, n):
        if n > self.size:
            raise ValueError('There are less cookies than asked to remove')
        else:
            self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

jar = Jar()
jar.deposit(10)
print(jar)
jar.withdraw(5)
print(jar)