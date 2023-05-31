"""Getting the Security Number
Given the Aadhar card number as the input. Check whether the sum of the digits of the Aadhar card number is even or odd.

If the sum is odd then there is a box1 which has 3 integers of size 5 which are security numbers for your Aadhar card number and the integers are 12321, 12345, and 56789. Check which of these is the palindrome number and hence it is your security number.

If the sum is even then there is a box2 which has 3 integers of size 5 which are security numbers for your Aadhar card number and the integers are 11111, 12345, and 99856. Check which of these is the perfect square number and hence it is your security number.

Input Format

Give the Aadhar card number as your input.

Output Format

Print the security number which satisfies the given conditions.

Constraints

The Aadhar card number must be 12 digits."""

aadhar_num = input()
sum_value = sum(list(map(int, [*aadhar_num])))
if sum_value % 2 == 1:
    print("12321")
elif sum_value % 2 == 0:
    print("99856")
