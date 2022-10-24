num = input()

l_sum = int(num[0]) + int(num[1])
r_sum = int(num[2]) + int(num[3])

if r_sum % l_sum == 0:
    print("YES")
else:
    print("NO")
