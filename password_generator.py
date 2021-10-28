from string import printable
from random import sample
symbols = printable
password = "".join(sample(symbols, int(input("Input a len of password: "))))
print("Your password is: " + password)
