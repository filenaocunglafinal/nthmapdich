from datetime import datetime

rightnow = datetime.now()
month_tracker1 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
month_tracker2 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]


def validate(mo):                                   # loop:  1: syntax error
    days = 31                                       #       2: another one
    if int(mo) < 0 or int(mo) > 12:                 #       3: already
        print("Wrong syntax dumb ass")
        monthif1 = input("Month: ")
        validate(monthif1)
    for i in range(12):
        if mo == "0":
            print("Fuck off")
            break
        elif mo == month_tracker1[i] and month_tracker1[i] == month_tracker2[i]:
            month_tracker2[i] = 0
            if i == 1:
                days -= 3
            elif i == 3 or i == 5 or i == 8 or i == 10:
                days -= 1

            def press(m):
                firstday = datetime(rightnow.year, int(m), 1)
                print("  SUN MON TUE WED THU FRI SAT", end="")
                day_i = int(firstday.strftime("%d")) - int(firstday.strftime("%w"))
                for i in range(6):
                    print("\n")
                    for i in range(7):
                        if day_i < 1 or day_i > days:
                            print('{0:4s}'.format("   x"), end="")
                            day_i += 1
                        else:
                            print('{0:4d}'.format(day_i), end="")
                            day_i += 1

            press(mo)
            print("\n")
            monthif2 = input("Month: ")
            validate(monthif2)
        elif mo == month_tracker1[i] and month_tracker2[i] == 0:
            print("Already shown that month")
            monthif3 = input("Month: ")
            validate(monthif3)


month = input("Enter the month of your will, else put 0: ")
validate(month)
