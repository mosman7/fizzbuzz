# Fizzbuzz
## Task:
Write a program that prints the numbers from 1 to 100.
For multiples of three print "Fizz" instead of the number
For the multiples of five print "Buzz" instead of the number
For numbers which are multiples of both three and five print "FizzBuzz".

First we set a range
```python
for x in range(1,101):        #goes through numbers in specified range
```
Then we find numbers divisible by both 3 and 5 and print fizzbuzz, we use the modulus function to find this,
if there is no remainer then the number is divisible by the both
```python
 if(x%3==0 and x%5==0):    #if number is divisible by both 3 and 5
      print("FizzBuzz")
```
Then we find numbers divisible by 3 and print fizz
```python
  elif(x%3 == 0):             #if number is divisible by 3
      print("Fizz")
```
Then we find the numbers divisible by 5 and print buzz
```python
 elif(x%5 == 0):             #if number is divisible by 5
      print("Buzz")
```
All other numbers that do not satisfy these 3 commands, we print the number. These are not divisible by either 3 or 5.
```python
  else:                         #if none of the conditions are satisfied, print number
      print(x)
```