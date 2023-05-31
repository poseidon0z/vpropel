"""To Divide Or Not
Alice likes all the numbers which are divisible by A. Bob does not like the numbers which are divisible by B and likes all the remaining numbers.

Determine the smallest number greater than or equal to N which is liked by both Alice and Bob.

Output -1 if no such number exists.

Input Format

The first and only line of each test case contains three space-separated integers A, B, and N — the parameters mentioned in the problem statement.

Output Format

Output the smallest number >= N which is divisible by A and is not divisible by B.

Output -1 if no such number exists."""

a, b, n = map(int, input().split())

if b % a == 0:
    print("-1")

else:
    if n % a == 0:
        i = n//a
    else:
        i = n//a + 1

    while True:
        num = a * i
        if num % b != 0:
            print(num)
            break
        i += 1
