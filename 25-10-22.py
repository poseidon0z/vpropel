from functools import reduce

levi_pos = int(input())

steps = input()

distance_moved = map(int, input().split())
total_distance = reduce(lambda a, b: a+b, distance_moved)

beast_pos = int(input())

final_pos = total_distance + levi_pos
if final_pos == beast_pos:
    print("Levi")
elif final_pos > beast_pos:
    print("Jaw")
elif final_pos < beast_pos:
    print("Beast")
