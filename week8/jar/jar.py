class Jar:
    def __init__(self, capacity=12, size=0):
        if capacity <= 0:
            raise ValueError("Capacity must be a Non Negative Integer")
        self._capacity = capacity
        self._size = size

    def __str__(self):
        return '🍪' * self.size

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError
        else:
            self._size += n

    def withdraw(self, n):
        if self.size - n < 0:
            raise ValueError
        else:
            self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
def main():
    jar = Jar(6)
    jar.deposit(3)
    jar.withdraw(1)
    print(jar)
    print(jar.capacity)
    print(jar.size)

if __name__ == "__main__":
    main()