class Jar:
    def __init__(self, capacity = 12, size = 0):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity
        self._size = 0


    def __str__(self):
         return "🍪" * self.size

    def deposit(self, n):
        if n + self.size > self.capacity:
            raise ValueError
        else:
            self._size += n


    def withdraw(self, n):
        if self.size - n < 0:
            raise ValueError
        else:
            self._size -=n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

def main():
    jar = Jar()
    print(jar)
    print(f" empty {jar.size}")
    jar.deposit(12)
    print(jar)
    print(f" after deposit {jar.size}")
    jar.withdraw(8)
    print(f" after withdraw {jar.size}")
    print(f" capacity {jar.capacity}")

if __name__ == "__main__":
    main()
