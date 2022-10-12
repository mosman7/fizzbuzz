for num in range(1,101):        #goes through numbers in specified range
    if(num%3==0 and num%5==0):    #if number is divisible by both 3 and 5
      print("FizzBuzz")
    elif(num%3 == 0):             #if number is divisible by 3
      print("Fizz")
    elif(num%5 == 0):             #if number is divisible by 5
      print("Buzz")
    else:                         #if none of the conditions are satisfied, print number
      print(num)