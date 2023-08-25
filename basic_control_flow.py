"""
Task 1 - basic math operations
Your task is to write a program which asks the user three times for a number. If number is even print ‘Even number’, else print ‘Odd number’.
"""

        
# def intORfloat(prompt):
#     while True:
#         value = input(prompt)
#         try:
#             return int(value)
#         except ValueError:
#             try:
#                 return float(value)
#             except ValueError:
#                 print('Enter a valid number !')


# for i in range(3):
    
#     odd_and_even_discriminator = intORfloat("Let's find out if the number is even or odd. Type in any number plaese. : ")

#     if odd_and_even_discriminator % 2 == 0:
#         print('This number is even')
#     else:
#         print('This number is odd')



"""
Task 2 - Calculate the sum of the numbers
Your task is to write a program which asks the user three times for a number and prints the sum of those numbers.
"""

# sum = 0

# for i in range(3):
    
#     num = int(input('Enter number: '))
    
#     sum += num

# print('Sum of the numbers: ', sum)




# def get_number(prompt):
#     value = input(prompt)
#     try:
#         return int(value)
#     except ValueError:
#         try:
#             return float(value)
#         except ValueError:
#             print('Please enter a valid number!')

# FirstNumber = get_number('This calculator adds any three given numbers. Please type in a first number.: ')

# while not isinstance(FirstNumber, (int, float)):
#     try:
#         FirstNumber = get_number('This calculator adds any three given numbers. Please type in a first number.: ')
#     except ValueError:
#         print('Please enter a valid number!')
        
# SecondNumber = get_number('Please type in a second number.: ')

# while not isinstance(SecondNumber, (int, float)):
#     try:
#         SecondNumber = get_number('Please type in a second number.: ')
#     except ValueError:
#         print('Please enter a valid number!')

# ThirdNumber = get_number('Please type in a third number.: ')

# while not isinstance(ThirdNumber, (int, float)):
#     try:
#         ThirdNumber = get_number('Please type in a third number.: ')
#     except ValueError:
#         print('Please enter a valid number!')
        
# result = FirstNumber + SecondNumber + ThirdNumber

# print("The result is : ",  result)





"""
Task 3 - Find the maximum number
Your task is to write a program which asks the user five times for a number and prints the maximum of those numbers.
"""

# Max = None

# for i in range(5):
    
#     num = int(input('Enter number: '))
    
#     if Max == None:
#         Max = num
#     if num > Max:
#         Max = num
    
        
# print('Maximum of the numbers: ', Max)
    


# first = input('Enter first number: ')
# second = input('Enter second number: ')
# third = input('Enter third number: ')
# forth = input('Enter forth number: ')
# fifth = input('Enter fifth number: ')

# print('Maximum of the numbers : ', max(first, second, third, forth, fifth))

"""
Task 4 - finding divisors of a number
Your task is to write a program which prints all the divisors of a number. The number comes from the user's input.
"""

# Num = int(input('Enter Number : '))

# divisors = list(range(1, 10000001))

# for i in divisors: 
#     if Num % i == 0 and Num >= i: 
#         print(i)

# Num = int(input('Enter Number : '))

# for i in range(1, Num+1):
    
#     if Num % i == 0:
#         print(i)

"""
Task 5 - Check if a number is even and divisible by 3
Your task is to write a program which asks the user for a number and prints if it is even and divisible by 3.
"""


# Num = int(input('Enter Number : '))

# if Num % 2 ==0 and Num % 3 ==0:
#     print(Num, "is even and divisible by 3.")
# else:
#     print(Num, "leaves the remainder:", Num % 3, "when divided by 3.")

"""
Task 6 - Check if a number is positive, odd and divisible by 7
Your task is to write a program which asks the user for a number and prints if a number is positive, odd and divisible by 7
"""

# Num = int(input('Enter a number: '))

# if not Num < 0 and not Num % 2 ==0 and Num % 7 ==0:
#     print(Num, "is positive, odd and  divisible by 7")



