n = int(input())

pair_count = 0
for i in range(n+1):
    if i % 2 == 0:
        pair_count += i//2
    else:
        pair_count += i//2
print(pair_count*2)
