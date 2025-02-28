class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return self.size * "🍪"

    def deposit(self, n):
        if (self.size + n > self.capacity):
            raise ValueError("Deposit Error")
        self.size = self.size + n

    def withdraw(self, n):
        if (self.size < n):
            raise ValueError("Withdraw Error")
        self.size = self.size - n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, n):
        if n < 1:
            raise ValueError("@capacity.setter error")
        self._capacity = n

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, n):
        if n > self.capacity:
            raise ValueError("@size.setter error")
        self._size = n


def main():
    jar = Jar()
    print(jar.size)
    jar.deposit(10)
    print(jar.size)
    jar.withdraw(4)
    print(jar.size)
    jar.deposit(4)
    print(jar.size)
    jar.deposit(1)
    print(jar.size)

if __name__ == "__main__":
    main()
