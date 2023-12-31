def square(number):
    """
    This function takes a number as input and returns its square.
    :param number: int or float
    :return: int or float, the square of the input number
    """  
    square = number ** 2
    return square 
square(2)
 

def reverse_string(s):
    """
    This function takes a string as input and returns its reverse.
    :param s: str
    :return: str, the reversed string
    """
    n = ''
    length = len(s)-1
    while length >= 0:
        n += s[length]
        length -= 1
    return n
reverse_string("hello")

def is_prime(n):
    """
    This function takes a number as input and returns True if the number is prime, otherwise False.
    :param n: int
    :return: bool, True if the number is prime, otherwise False
    """

    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True
is_prime(3)

def factorial(n):
    """
    This function takes a number as input and returns its factorial.
    :param n: int
    :return: int, the factorial of the input number
    """
   
    total = 1
    for i in range(1,n+1):
        total *= i
    return total

def find_maximum(lst):
    """
    This function takes a list of numbers lst and returns the maximum number in the list.
    :param lst: list of int
    :return: int, the maximum number in the list
    """
    if not lst:
        return None 
    max_num = lst[0]  
    for num in lst:
        if num > max_num:
            max_num = num
    return max_num



def odd_or_even(n):
    """
    This function takes a number n and returns "Odd" if the number is odd and "Even" if the number is even.
    :param n: int
    :return: str, "Odd" or "Even"
    """
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

def is_palindrome(s):
    """
    This function takes a string `s` and returns `True` if the string is a palindrome, and `False` otherwise. 
    A palindrome is a word or phrase that reads the same backward as forward.
    
    :param s: str
    :return: bool, `True` if the string is a palindrome, `False` otherwise.
    """

    ss=""
    for i in range(len(s)):
        ss+=s[len(s)-i-1]
    if ss ==s:
        return True
    else:
        return False



def find_gcd(a, b):
    """
    This function takes two positive integers `a` and `b` and returns their greatest common divisor (GCD).
    
    :param a: int
    :param b: int
    :return: int, the greatest common divisor of `a` and `b`.
    """
    divisor=0
    if a > b:
        for i in range(1,b+1):
            if a % i == 0 and b % i == 0:
                divisor = i
            
    if b > a:
        for i in range(1,a+1):
            if a % i == 0 and b % i == 0:
                divisor = i
    return divisor 




