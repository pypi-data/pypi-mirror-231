class Calculator:   #Calcluator class to add, subtract, multiply, divide and calculate the nth root of a real number.
    def __init__(self):
        self.memory = 0.0

    def add(self, number: float) -> float:
        """Add number to value in memory."""
        self.memory += number
        return self.memory

    def subtract(self, number: float) -> float:
        """Subtract number from value in memory."""
        self.memory -= number
        return self.memory

    def multiply(self, number: float) -> float:
        """Multiply number by value in memory."""
        self.memory *= number
        return self.memory

    def divide(self, number: float) -> float:
        """Divide value in memory by a number."""
        if number == 0:  #Cannot divide by zero.
            raise ValueError("Division by zero is not allowed.")
        self.memory /= number
        return self.memory

    def nth_root(self, number: float) -> float:
        """Calculate nth root of value in memory."""
        if number <= 0:
            raise ValueError("Root must be a positive integer.")
        if self.memory <0 and number % 2 == 0:
            raise ValueError("Cannot calculate even root of negative integer.")
        self.memory **= 1 / number #Result should be x^1/y = n or for example, 4^1/2 = 2
        return self.memory

    def reset_memory(self):
        """Reset default memory value to 0."""
        self.memory = 0.0
        return self.memory