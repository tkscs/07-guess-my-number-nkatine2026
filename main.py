# the user will choose a number
# this program will guess the number
# the user will say "yes" or "higher" or "lower"
# the program will ask to play again or exit
i = 0
while True:
    w = input(f"is your number {i}?")
    if w == "lower":
        i = i-1
    if w == "higher":
        i = i+1
    if w == "yes": break 
print("yay")
         