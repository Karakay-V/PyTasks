import math

def taskThird():
    def square_root(numbers):
        result = []
        n = len(numbers)
        for i, number in enumerate(numbers):
            print(f"Processing number: {number}")
            result.append(math.sqrt(number))
            print(f"Completed: {int((i + 1) / n * 100)}%")
        return result

    numbers = [1, 4, 9, 16, 25, 36, 49, 64, 81]
    square_root(numbers)

    return "end"