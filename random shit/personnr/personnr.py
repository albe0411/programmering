num = 0
count = 0

while True:
    try:
        personnr = input(": ")

        while True:
                if personnr[count].isnumeric():
                    if count % 2 == 0:
                        if int(personnr[count]) * 2 > 9:
                            for x in str(int(personnr[count]) * 2):
                                num += int(x)
                        else:
                            num += int(personnr[count]) * 2
                    else:
                        num += int(personnr[count])
                    count += 1
                else:
                    personnr = personnr.replace(personnr[count], "")

                if count == 9:
                    break

        if int(personnr[-2]) % 2 == 0:
            print("female")
        else:
            print("male")

        kontrol_siffra = (10 - (num % 10)) % 10
        if kontrol_siffra == int(personnr[-1]):
            print("valid")
        else:
            print("invalid")

    except ValueError:
        print("ValueError")
    except IndexError:
        print("IndexError")
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
        break
    except:
        print("error")