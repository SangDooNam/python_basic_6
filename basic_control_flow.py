"""
Task 1 - basic math operations
Your task is to write a program which asks the user three times for a number. If number is even print ‘Even number’, else print ‘Odd number’.
"""
# while True:
#     try:
#         odd_and_even_discriminator = int(input("Let's find out if the number is even or odd. Type in any number plaese. : "))


#         if odd_and_even_discriminator % 2 == 0:
#             print('This number is even')
#         else:
#             print('This number is odd')
            
#         break
#     except ValueError: 
#         print('That was not a valid number. Pleas type in an integer.')
        


"""
Task 2 - Calculate the sum of the numbers
Your task is to write a program which asks the user three times for a number and prints the sum of those numbers.
"""

# FirstNumber = int(input('This calculator adds any three given numbers. Please type in the first number.: '))

# if FirstNumber == int or float:
    
#     SecondNumber = int(input("Please type in the second number.: " ))
    
#     if SecondNumber == int or float:
        
#         ThirdNumber = int(input("Please type in the third number.: " ))
        
#         if ThirdNumber == int or float:
#             print("The result is : ", FirstNumber + SecondNumber + ThirdNumber)
                
# try:
    # FirstNumber = int(input('This calculator adds any three given numbers. Please type in the first number.: '))

    # if FirstNumber == int or float:
        
    #     SecondNumber = int(input("Please type in the second number.: " ))
        
    #     if SecondNumber == int or float:
            
    #         ThirdNumber = int(input("Please type in the third number.: " ))
            
    #         if ThirdNumber == int or float:
    #             print("The result is : ", FirstNumber + SecondNumber + ThirdNumber)
                

# except:
#     FirstNumber = float(input('This calculator adds any three given numbers. Please type in the first number.: '))

#     if FirstNumber == int or float:
        
#         SecondNumber = float(input("Please type in the second number.: " ))
        
#         if SecondNumber == int or float:
            
#             ThirdNumber = float(input("Please type in the third number.: " ))
            
#             if ThirdNumber == int or float:
#                 print("The result is : ", FirstNumber + SecondNumber + ThirdNumber)
                
# except ValueError: 
#     print('That was not a valid number. Pleas type in an integer or float.')
    


"""
Task 3 - Find the maximum number
Your task is to write a program which asks the user five times for a number and prints the maximum of those numbers.
"""

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