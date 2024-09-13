import re
print(" when its position : " , "1  2  3  4  5  6  7  8  9   12")
print("--------------------------------------------------------------------------------------")
def thrice(match):
    number = int(match.group(0))
    return str(number**3)
print("thrice the number : " , re.sub(r"\d+" , thrice , "1 2 3 4 5 6 7 8 9 12"))
def square(match):
    number = int(match.group(0))
    return str(number**2)
print("twice the number : " , re.sub(r"\d+" , square , "1  2  3  4  5  6   7   8   9   12"))

