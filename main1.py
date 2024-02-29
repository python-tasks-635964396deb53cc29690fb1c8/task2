sp1 = list(map(int, input().split()))
sp2 = list(map(int, input().split()))
print(f'Общее (кол-во): {len(set(sp1).intersection(set(sp2)))}')
