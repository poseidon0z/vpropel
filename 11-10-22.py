num1 = int(input())
num2 = int(input())

# num1_factors = []
# num2_factors = []
# for i in range(2,num1):
#     if num1%i == 0:
#         num1_factors.append(i)

# for i in range(2,num2):
#     if num2%i == 0:
#         num2_factors.append(i)

# num1_sum = 0
# num2_sum = 0

# for i in num1_factors:
#     num1_sum += i

# for i in num2_factors:
#     num2_sum += i

num1_factors = [i for i in range(2, num1) if num1 % i == 0]
num2_factors = [i for i in range(2, num2) if num2 % i == 0]

num1_sum = sum(num1_factors)
num2_sum = sum(num2_factors)

if num1_sum > num2_sum:
    print(num1)
elif num2_sum > num1_sum:
    print(num2)
else:
    print("No dominance")
