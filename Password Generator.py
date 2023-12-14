import random # we import random to generate randoms values from the lists


uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" # this are the letter that we are gonna to use
lowercase_letters = uppercase_letters.lower() # we conver the upper in lower letters reusing the varibale uppercase

digits = "0123456789" # 
symbols = "()[]{},:;-/?+*#"

upper, lower, nums, sym, = True, False, True, True

all= ""

if upper:
    all += uppercase_letters
elif lower:
    all += lowercase_letters
elif nums:
    all += digits
elif sym:
    all += symbols

length = 20
amount = 10

for x in range(amount):
    password = "".join(random.sample(all, length))
    print(password)


