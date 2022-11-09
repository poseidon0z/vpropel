"""Midnumeral Strings to Rightnumeral Strings (D)
Midnumeral string is a string which contains one number in between letters. For example, a1b2c is a midnumeral string. A midnumeral strings may contain letters a to z, numbers 1 to 9 and both left and the right parentheses.

Rightnumeral string is a string which can be formed from midnumeral string:

(i) All the characters except left and right parenthesis in the midnumeral string is present in rightnumeral string.

(ii) A number ‘n’ which is between letters ‘a’ anb ‘b’ in the midnumeral string will appear in the right hand of side of the letters ‘a’ and ‘b’ in rightnumeral string in a particular fashion.

During the process of conversion of a midnumeral string to a rightnumeral string, a waiting stream is used.

Given a midnumeral string ‘m’ it can be converted to a rightnumeral string ‘r’ as follows:

Process character by character of midnumeral string ‘m’.

When a letter is seen add it to rightnumeral string ‘r’.

When a number ‘n’ is seen and waiting stream is empty or the recently added character to waiting stream is left parenthesis then add ‘n’ to waiting stream

If a number ‘n’ seen and there are some numbers in the waiting stream then

If the recently added numeral in waiting stream is less than ‘n’ then add ‘n’ to waiting stream

Otherwise process waiting stream from most recent to least recent:

Remove number from waiting stream and add it to ‘r’

Repeat part (i), until the recent value available in waiting stream is less than ‘n’ or the recent character the waiting stream is left parenthesis or the waiting stream becomes empty

Add ‘n’ to the waiting stream

c) If a left parenthesis is seen then add it to waiting stream

d) When right parenthesis is seen then remove all numbers from most recent to least recent from waiting stream and add it to r till left parenthesis is seen. Discard left and right parenthesis

4. When the end of the midnumeral ‘m’ string is reached remove all numerals from most recent to least recent from waiting stream and add it to right numeral string ‘r’

For example,

a1b2c will be abc21

a2b1c will be ab2c1

(a1b)2c will be ab1c2

a1b4(c5d2e)7f will be abcd5e2f741

Note: All the characters in the midnumeral will be distinct and only valid input is given

Input Format

First line contains the midnumeral string, m

Output Format

First line should contain the rightnumeral string, r"""


midnumeral_string = input()

rightnumeral_string = ""
waiting_stream = ""

for character in midnumeral_string:
    run = True
    while run is True:
        if character.isalpha():
            rightnumeral_string += character
        elif character.isnumeric():
            if waiting_stream == "" or waiting_stream[-1] == "(":
                waiting_stream += character
            elif int(character) > int(waiting_stream[-1]):
                waiting_stream += character
            else:
                rightnumeral_string += waiting_stream[-1]
                waiting_stream = waiting_stream[:-1]
                continue
        elif character == "(":
            waiting_stream += character
        elif character == ")":
            for i in range(len(waiting_stream)-1, -1, -1):
                if waiting_stream[i].isnumeric():
                    rightnumeral_string += waiting_stream[i]
                    waiting_stream = waiting_stream[:-1]
                elif waiting_stream[i] == "(":
                    waiting_stream = waiting_stream[:-1]
                    break
        run = False

for character in waiting_stream[::-1]:
    rightnumeral_string += character

print(rightnumeral_string)
