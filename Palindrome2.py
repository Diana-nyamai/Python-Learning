#palindrome leetcode problem
def Palindrome(num):
    number = str(num)
    rString = number[::-1]
    #my mistake was converting it back to integer

    if rString == num:
        return True
    else:
        return False
    
        

number = input('Enter a number: ')
print(Palindrome(number))


