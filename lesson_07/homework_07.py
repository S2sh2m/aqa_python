# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    if number <= 0:
        print("Numbers should be 1 or more ")

    multiplier = 1
    while number * multiplier <=25:
        result = number * multiplier
        print(f"{number}x{multiplier}={result}")
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def sum_of_two (a=1, b=5):
    return a+b
# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def average (numbers):
    return sum(numbers) / len(numbers)
# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse_input():
    data = input("Input smth pls: " )
    return data[::-1]
# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def long_word(word):
    return max(word, key=len)
# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):

    return str1.find(str2)

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
# task 8
# task 9
# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""

def build_multiplication_table(number: int, max_product: int = 25):
    lines=[]
    multiplier = 1
    while number*multiplier <=max_product:
        result = number *multiplier
        lines.append(f"{number}x{multiplier}={result}")
        multiplier +=1
    return lines

def sum_two_numbers(first: float, second: float) -> float:
    return first + second

def average_of(numbers: list[float]) -> float:
    return sum(numbers) / len(numbers) if numbers else 0.0

def longest_word(words: list[str]) -> str | None:
    return max(words, key=len) if words else None