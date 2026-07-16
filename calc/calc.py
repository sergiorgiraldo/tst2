def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


if __name__ == "__main__":
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    print("Add result:", add(x, y))
    print("Subtract result:", subtract(x, y))
    print("Multiply result:", multiply(x, y))
