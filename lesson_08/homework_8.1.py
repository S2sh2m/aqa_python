from os.path import split

arr = ["1, 2, 3, 4", "1, 2, 3, 4, 50", "qwerty1, 2, 3"]

def sum_string(s) :
    try:
        numbers = s.split(",")
        return sum(int(num) for num in numbers)
    except ValueError:
        return "Не можу це зробити"

result = [sum_string(item) for item in arr]
print(result)
