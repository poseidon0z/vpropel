"""Levi Vs Beast Titan
Levi being surrounded by many other medium size titans and he is aiming to kill the Beast Titan. For him to do this he has to kill all other Titan within a limited amount of gas. Given the number of titans, amount of gas he has and the number of time Levi jumps by using gas machine to kill each titan find whether at the end he would be left with enough gas to kill the Beast Titan or not. Note with every jump 0.5 litre of gas is used.

Input Format
First line contains two space separated values n and l namely number of titans and amount of gas Levi has initially.

Second line contains n space separated values denoting number of times Levi must jump to kill each titan.

Output Format
•    Print YES or No based on the fact that Levi will be able to defeat the Beast Titan or not."""
n, l = map(int, input().split())
jumps = list(map(int, input().split()))

total_jumps = sum(jumps)
if total_jumps * 0.5 <= l:
    print("YES")
else:
    print("NO")
