"""
How to find the sum of digits of a positive integer number using recursion
ex:54 = 5+4=9
ex:364 = 3+6+4=13
"""
def sum_of_digits(number):
    if number == 0:
        return 0
    else:
        return int(number%10) + sum_of_digits(int(number//10))


def power(number,power_num):
    if power_num == 0 :
        return 1
    return number * power(number,power_num - 1)


"""
Write a function called (productOfArray) which takes
in an array of numbers and returns the product of them all.
Examples
productOfArray([1,2,3]) #6
productOfArray([1,2,3,10]) #60
"""
def product_of_array(arr:list,index=0):
    if index == len(arr):
        return 1
    else:
        return arr[index] * product_of_array(arr,index+1)


"""
Write a function called (recursiveRange) which accepts a number
and adds up all the numbers from 0 to the number passed to the function.
"""
def recursiveRange(num):
    if num == 0:
        return 0
    return num + recursiveRange(num-1)


"""
Write a recursive function called reverse which accepts a string and
returns a new string in reverse.
Examples
reverse('python') # 'nohtyp'
reverse('appmillers') # 'srellimppa'
"""
def reverse(str:str,index=-1):
    if index == -len(str)-1:
        return ""
    return str[index] + reverse(str,index-1)


"""
Write a recursive function called isPalindrome which returns
true if the string passed to it
is a palindrome (reads the same forward and backward). Otherwise it returns false.
Examples
isPalindrome('awesome') # false
isPalindrome('tacocat') # true
"""
def isPalindrome(str:str,index=-1):
    if index == -len(str)-1:
        return''
    end= str[index] + isPalindrome(str,index-1) 
    if end == str:
        return True
    elif end != str and index == -1:
        return False
    else:
        return end

