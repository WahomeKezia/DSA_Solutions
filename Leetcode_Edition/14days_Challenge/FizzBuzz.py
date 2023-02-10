def fizzbuzz(n):
    # loop through the range of numbers from 1 to n (inclusive)
    for i in range(1, n+1):
        # check if the number is a multiple of both 3 and 5
        if i % 3 == 0 and i % 5 == 0:
            # if yes, print "fizzbuzz"
            print("fizzbuzz")
        # check if the number is a multiple of 3 (but not 5)
        elif i % 3 == 0:
            # if yes, print "fizz"
            print("fizz")
        # check if the number is a multiple of 5 (but not 3)
        elif i % 5 == 0:
            # if yes, print "buzz"
            print("buzz")
        # if the number is not a multiple of 3 or 5
        else:
            # print the value of i
            print(i)
n= 20
res = fizzbuzz(n)
#print(res) anding this print statement caused the solution to print out a none at the end
# the range number