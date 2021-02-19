item1 = int(input("Enter price of the first item: "))
item2 = int(input("Enter price of the second item: "))

club_card = input("Does customer have a club card? (Y/N): ")

tax_rate = float(input("Enter tax rate, e.g. 5.5 for 5.5% tax: "))

base_price = (item1 + item2)

if (item1 > item2):
    total_after_discount = item1 + item2 * .5
else:
    total_after_discount = item1 * .5 + item2

if (club_card == "Y" or club_card == "y"):
    total_after_discount = total_after_discount - total_after_discount * .1
else:
    total_after_discount = total_after_discount

total_tax = total_after_discount * (tax_rate / 100)

total_price = str(round(total_after_discount + total_tax, 2))

print("Base price =  {:2.2f}".format(base_price), sep="")
print("Price after discounts = {:2.2f}".format(total_after_discount), sep="")
print("Total price = ", total_price, sep="")
