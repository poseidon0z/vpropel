alphabet_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
                 "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

test_cases = int(input())

for i in range(test_cases):
    text, code = input().split()

    change_list = alphabet_list[:]
    new_chars = []

    for letter in code:
        if letter in new_chars:
            continue
        new_chars.append(letter)

    for letter in new_chars:
        for a in range(len(change_list)):
            if change_list[a] == letter:
                change_list.pop(a)
                break

    change_list = new_chars + change_list

    answer = ""
    for letter in text:
        ind = alphabet_list.index(letter)
        answer += change_list[ind]
    
    print(answer)
