num = input()
div_num = len(num)
print(div_num)
answer_bool = True
for i in range(len(num)):
    print(int(num[:i+1]))
    if int(num[:i+1]) % div_num != 0:
        answer_bool = False

if answer_bool == True:
    print("Yes")
else:
    print("No")
