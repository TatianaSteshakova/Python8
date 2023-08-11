N = int(input("Введите n: "))

numbers = []

print("Введите числа: ")
for _ in range(N):
    num = int(input())
    numbers.append(num)

numbers.reverse()

txt = ""

for num in numbers:
    txt += str(num) + " "

print(txt)