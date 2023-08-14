N = int(input("Введите n: "))

numbers = []

print("Введите числа: ")
for _ in range(N):
    num = int(input())
    numbers.append(num)

length = len(numbers)

new = [0] * length

for i in range(length):
     new[(i + 1) % length] = numbers[i]

txt = ""

for num in new:
      txt += str(num) + " "

print(txt)