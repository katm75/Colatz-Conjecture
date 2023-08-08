number = 3
steps = 0

for i in range(200):
    if number == 1:
        break
    # go to print statement because calculation is done
    elif number % 2 == 0:
    #is the number even?
        number = number / 2
    # then do this operation
        steps = steps + 1
    else:
    # then it's odd so do this
        number = (3 * number) + 1
        steps = steps + 1
    
if number == 1:
    print("It took", steps, "steps")
else:
    print("The number didn't reach 1 yet")