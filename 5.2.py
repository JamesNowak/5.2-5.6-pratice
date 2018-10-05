# This is the main organizer of the program
def main():
    monthly()


def monthly():
    var1 = float(input("How much do you spend on grocieries a month?: "))
    var2 = float(input("How much do you spend on gas a month?: "))
    var3 = float(input("How much do you spend on going out a month?: "))
    monthly_total = var1 + var2 + var3
    yearly(monthly_total)


def yearly(monthly_total):
    print("It will cost you", (monthly_total * 12), "dollars a year.")


main()
