from Clock import Clock


def main():
    #kivetelkezeles
    try:
        hour = int(input("Add meg az órát: "))
        minute = int(input("Add meg a percet: "))
        second = int(input("Add meg a másodpercet: "))

        if hour < 0 or hour > 23 or minute < 0 or minute > 59 or second < 0 or second > 59:
            raise Exception()
        else:

            #ora objektum letrehozasa, idokiirasa
            clock = Clock(hour, minute, second)
            clock.showTime()

    except:
        print("A bemenet nem  megfelelő")


if __name__ == '__main__':
    main()

