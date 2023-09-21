class Calculator:
    """
    A Calculator class consisting of functions to perform basic arithmetic calculations
    """
    def __init__(self):
        self.memory = 0

    def add(self, n):
        """
        Addition function which adds n to the memmory

        >>> calculator = Calculator()
        >>> calculator.add(10)
        0.0 + 10 = 10.0
        10
        """
        temp_memory = self.memory
        self.memory += n
        self.memory = round(self.memory, 15)
        print(f"{temp_memory:.1f} + {n} = {self.memory:.1f}")
        return self.memory

    def subtract(self, n):
        """
        Subtraction function which removes n from the memory

        >>> calculator = Calculator()
        >>> calculator.add(5)
        0.0 + 5 = 5.0
        5
        >>> calculator.subtract(2)
        5.0 - 2 = 3.0
        3
        """
        temp_memory = self.memory
        self.memory -= n
        self.memory = round(self.memory, 15)
        print(f"{temp_memory:.1f} - {n} = {self.memory:.1f}")
        return self.memory

    def multiply(self, n):
        """
        Multiplication function which multiplies memory by n

        >>> calculator = Calculator()
        >>> calculator.add(5)
        0.0 + 5 = 5.0
        5
        >>> calculator.multiply(5)
        5.0 * 5 = 25.0
        25
        """
        temp_memory = self.memory
        self.memory *= n
        self.memory = round(self.memory, 15)
        print(f"{temp_memory:.1f} * {n} = {self.memory:.1f}")
        return self.memory

    def divide(self, n):
        """
        Division function which divides memory by n

        >>> calculator = Calculator()
        >>> calculator.add(6)
        0.0 + 6 = 6.0
        6
        >>> calculator.divide(2)
        6.0 / 2 = 3.0
        3.0
        """
        if n == 0:
            raise ValueError("Can't divide by 0")
        temp_memory = self.memory
        self.memory /= n
        self.memory = round(self.memory, 15)
        print(f"{temp_memory:.1f} / {n} = {self.memory:.1f}")
        return self.memory

    def n_root(self, n):
        """
        Root function which takes n root from memory value

        >>> calculator = Calculator()
        >>> calculator.add(625)
        0.0 + 625 = 625.0
        625
        >>> calculator.n_root(4)
        625.0 ^ (1/4) = 5.0
        5.0
        """
        if n == 0:
            raise ValueError("Can't take root of 0")
        temp_memory = self.memory
        self.memory **= (1/n)
        self.memory = round(self.memory, 15)
        print(f"{temp_memory:.1f} ^ (1/{n}) = {self.memory:.1f}")
        return self.memory

    def reset(self):
        """
        Reset function which resets memory to 0

        >>> calculator = Calculator()
        >>> calculator.add(16)
        0.0 + 16 = 16.0
        16
        >>> calculator.reset()
        Memory cleared
        0
        """
        self.memory = 0
        print("Memory cleared")
        return self.memory

c = Calculator()
