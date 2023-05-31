"""Manipulating the list
You are given a sorted list X of size n. You have to make a new list Y such that Y[i] is equal to the number of elements strictly greater than X[i] in list X.

Print the new list.

Input Format

The first line of each test case consists of one integer denoting n, where n is the size of the list given to you.

The second line of each test case contains the list given to you containing n elements.

Output format

In a single line print all the elements of the array Y in a space separated format.
"""

n = int(input())
X = list(map(int, input().split()))
Y = []

for i in range(n):
    count = 0
    for a in range(n):
        if X[a] > X[i]:
            count += 1
    Y.append(str(count))

print(" ".join(Y))
