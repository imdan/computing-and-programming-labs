print("Please enter the number of coins:")

quarters = int(input("# of quarters: "))
dimes = int(input("# of dimes: "))
nickels = int(input("# of nickels: "))
pennies = int(input("# of pennies: "))

total_cents = quarters * 25 + dimes * 10 + nickels * 5 + pennies * 1

dollars = total_cents // 100
cents = total_cents % 100

print("The total is ", dollars, "dollars and ", cents, "cents")
