count = int(input('Количество: '))
data = dict()

for i in range(count):
    key, value = input().split()
    data[key] = value

search = input()

for k, v in data.items():
    if k == search or v == search:
        print(k, v)
