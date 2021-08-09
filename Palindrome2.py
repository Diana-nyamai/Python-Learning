#palindromeu
def Palindrome(num):
    number = str(num)
    rString = number[::-1]

    if rString == num:
        return True
    else:
        return False
    
        

number = input('Enter a number: ')
print(Palindrome(number))


