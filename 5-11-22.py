"""IP Address
Suppose you are an intern at a Cyber Security Lab. You are given some IP Addresses and you need to check if it is in the correct format to be used as a proxy or not.

For an IP Address to be correct it should satisfy the following conditions:

It should contain 4 integers, separated by a full stop (.)

It cannot have spaces.

All the integers must be in the range 0 to 255

Hint: Take IP as String Input then split them.

Input Format:

First line contains the number of test cases.
Each contain a single line input of an IP Address

 

Output Format:

If the IP is correct Print “Can Be Used as a Proxy”.

If not then print “Cannot be used as a Proxy”."""

n = int(input())
for i in range(n):
    ip = input()
    conditions_met = True
    if len(ip.split(".")) != 4 or " " in ip:
        conditions_met = False
    for i in ip.split("."):
        try:
            if int(i) < 0 or int(i) > 255:
                conditions_met = False
        except ValueError:
            conditions_met = False
    if conditions_met:
        print("Can Be Used as a Proxy")
    else:
        print("Cannot Be Used as a Proxy")
