num = input()
div_num = len(num)
answer_bool = True
for i in range(len(num)):
    if int(num[:i+1]) % div_num != 0:
        answer_bool = False
    div_num -= 1

if answer_bool == True:
    print("Yes")
else:
    print("No")
