import sys

class Jar:


    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0


    def __str__(self):
        total_cookies = ""
        for x in range(self.size):
            total_cookies += "🍪"
        return total_cookies

    def deposit(self, n):

        if n + self.size <= self.capacity:
            self.size += n
        else:
            raise ValueError("ValueError")

    def withdraw(self, n):
        # Removes N cookies from the jar, if not that many raise valueError

        if n <= self.size:
            self.size -= n
        else:
            raise ValueError("ValueError")


    @property
    def capacity(self):
        # return capacity
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("ValueError")
        else:
            self._capacity = capacity


    def size():
        # return how many cookies there are
        return self.size


def main():
    jar_one = Jar(5)
    print(jar_one.capacity)
    jar_one.deposit(3)
    print(jar_one)
    jar_one.withdraw(2)
    print(jar_one)
    jar_one.withdraw(2)
    print(jar_one)



if __name__ == "__main__":
    main()


