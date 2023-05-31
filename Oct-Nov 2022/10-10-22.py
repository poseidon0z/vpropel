name = [*input()]
seats = int(input())

seat_letters = {}

program_complete = False

i = 0
seats_list = list(range(1, seats+1))
reverse_list = list(range(seats, 0, -1))
seats_list += reverse_list
for seat in seats_list:
    index_value = i % len(name)
    try:
        if seat_letters[seat] == name[index_value]:
            print(seat)
            program_complete = True
            break
    except:
        seat_letters[seat] = name[index_value]
    i += 1

if program_complete == False:
    print(-1)
