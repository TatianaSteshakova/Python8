N = int(input("Введите n: "))

numbers = []

print("Введите числа: ")
for _ in range(N):
    num = int(input())
    numbers.append(num)

length = len(numbers)
start = 0
end = length - 1

while start < end:
        numbers[start], numbers[end] = numbers[end], numbers[start]
        start += 1
        end -= 1

txt = ""

for num in numbers:
      txt += str(num) + " "

print(txt)