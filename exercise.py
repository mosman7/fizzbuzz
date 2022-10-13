for x in range(1,101):        #goes through numbers in specified range
    if(x%3==0 and x%5==0):    #if number is divisible by both 3 and 5
      print("FizzBuzz")
    elif(x%3 == 0):             #if number is divisible by 3
      print("Fizz")
    elif(x%5 == 0):             #if number is divisible by 5
      print("Buzz")
    else:                         #if none of the conditions are satisfied, print number
      print(x)