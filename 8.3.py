boat = int(input("Введите переносимую массу лодки: "))
traveler = int(input("Введите кол-во путешественников: "))

weights = 0

print("Введите вес каждого путешественника:")
for i in range (0, traveler):
    n = int(input())
    weights += n

boat_weights = 0
cnt = 0

while boat_weights < weights:
    cnt += 1
    boat_weights += boat

print("Требуется лодок:", cnt)