#Write a program to print “Bright IT Career” ten times using for loop
'''
for i in range(10):
    print("Bright IT Career")
'''

# program to print 1 to 20 numbers using the while loop
'''
i = 1
while i < 21:
  print(i)
  i += 1
'''

#program to print the odd and even numbers
'''
num = int(input(" Please Enter the Maximum Number for Odd Numbers: "))
 
for number in range(1, num+1):
    if(number % 2 != 0):
        print("{0}".format(number))
num = int(input(" Please Enter the Maximum Number for Even Numbers : "))
 
for number in range(1, num+1):
    if(number % 2 == 0):
        print("{0}".format(number))        
'''

#program to printt even an odd numbers without using if statement
'''
num = int(input(" Please Enter the Maximum Number for Even Numbers : "))
 
for number in range(2, num+1, 2):
    print("{0}".format(number))
    
num = int(input(" Please Enter the Maximum Number for Odd Numbers: "))    

for number in range(1, num + 1, 2):
    print("{0}".format(number))    
'''

# program to print largest number among three numbers.
'''
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

print("The largest number is", largest)
'''

#program to print even number between 10 and 100 using while
'''
num = 100
number = 10
 
while number <= num:
    if(number % 2 == 0):
        print("{0}".format(number))
    number = number + 1
'''

#Python program to find Armstrong number or not
'''
num = int(input("Enter a number: "))
order = len(str(num))
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** order
   temp //= 10
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
'''

#program to find prime or not
'''
number = int(input("Enter any number: "))
if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print(number, "is not a prime number")
            break
    else:
        print(number, "is a prime number")
else:
    print(number, "is not a prime number")
'''

# program to palindrome or not
'''
string=input(("Enter a string:"))  
if(string==string[::-1]):  
      print("The letter is a palindrome")  
else:  
      print("The letter is not a palindrome") 
'''

