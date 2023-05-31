# Why tf are there so many anime reference questions for no reason smhsmh
"""Hungry Naruto
Naruto is very hungry. So, Naruto goes to a shop selling burgers. The shop has 2 types of burgers:

Normal burgers, which cost X rupees each

Premium burgers, which cost Y rupees each (where Y > X)

Naruto has R rupees. Naruto wants to buy exactly N burgers. He also wants to maximize the number of premium burgers he buys. Determine the number of burgers of both types Naruto must buy.

Output -1 if it is not possible for Naruto to buy N burgers.

Input Format

The first and only line of each test case contains four space-separated integers X, Y, N, and R — the cost of a normal burger, the cost of a premium burger, the number of burgers Naruto wants to buy and the amount of money Naruto has.

​Output Format

For each test case, output on a new line two integers: the number of normal burgers and the number of premium burgers Naruto must buy satisfying the given conditions.

Output -1 if he cannot buy N burgers."""


def solution():
    norm_cost, prem_cost, n, balance = map(int, input().split())

    if balance // norm_cost < n:
        print(-1)
        return

    for i in range(n+1):
        if prem_cost * (n-i) + norm_cost * i <= balance:
            print(i, n-i)
            break


solution()
