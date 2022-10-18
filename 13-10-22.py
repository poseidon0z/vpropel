normal_time, secondary = input().split(" ")


def converter(item):
    if len(item) == 1:
        item = "0" + item
    return item


time_list = normal_time.split(":")
hours, minute, sec = int(time_list[0]), int(time_list[1]), int(time_list[2])

if secondary == "P.M":
    hours += 12
elif secondary == "midnight":
    hours = 24

thing = hours // 8

heaven_secondary = ""
if secondary == "midnight":
    heaven_secondary = "midnight"
elif hours == 8 and minute == 0 and sec == 0:
    heaven_secondary = "midmorning"
elif hours == 16 and minute == 0 and sec == 0:
    heaven_secondary = "midevening"
else:
    # match thing:
    #     case 0:
    #         heaven_secondary = "A.M"
    #     case 1:
    #         heaven_secondary = "B.M"
    #     case 2:
    #         heaven_secondary = "C.M"
    if thing == 0:
        heaven_secondary = "A.M"
    elif thing == 1:
        heaven_secondary = "B.M"
    elif thing == 2:
        heaven_secondary = "C.M"

heaven_time = [str(hours - (thing * 8)), str(minute), str(sec)]
if secondary == "midnight":
    heaven_time[0] = "8"
elif hours == 8 and minute == 0 and sec == 0:
    heaven_time[0] = "8"
elif hours == 16 and minute == 0 and sec == 0:
    heaven_time[0] = "8"

print(converter(heaven_time[0]) + ":" + converter(heaven_time[1]
                                                  ) + ":" + converter(heaven_time[2]) + " " + heaven_secondary)
