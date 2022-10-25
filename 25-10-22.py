"""Levi vs Titans
Levi has to kill the beast titan for which he has to reach its Nape.If he is short of distance the Beast titan will kill him.If he goes past his nape,the Jaw titan will kill him.

Given his starting position,number of moves made by him,distance moved by him in each move and position of Beast titan, find if he kills Beast titan or not.

If Levi kills the Beast ,print Levi.

If he falls short of the distance, print Beast

If he goes past the Beast Titan, print Jaw

Input Format

The first line contains position of Levi

Second line contains number of moves made by Levi

Third line contains the distance covered by Levi in each move separated by a space

Fourth line contains position of the Beast titan.

Output Format

Levi / Beast /Jaw
"""

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
