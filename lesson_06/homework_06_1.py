print("Input some text")
symbols = input()
uniq = set(symbols)
count = len(uniq)
print(count>10)

#OR

symbols = input("Input some text to count: ")

uniq = []

for char in symbols:
    if char not in uniq:
        uniq.append(char)

count = len(uniq)
print(count>10)