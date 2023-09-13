def square(number):
    """
    This function takes a number as input and returns its square.
    :param number: int or float
    :return: int or float, the square of the input number
    """
    def 
    pass  
    def square(number):
        number = input("type a number or a word: ")
        square = number ** 2
    print(square)  
    square(number)


def reverse_string(s):
    """
    This function takes a string as input and returns its reverse.
    :param s: str
    :return: str, the reversed string
    """
    pass
    
    def reverse_string(s):
        s = str(input("type a word: "))
        n = ''
        length = len(n)-1
        while length >= 0:
            n += n[length]
            length -= 1
        print(n)
        reverse_string(s)
    
    


def is_prime(n):
    """
    This function takes a number as input and returns True if the number is prime, otherwise False.
    :param n: int
    :return: bool, True if the number is prime, otherwise False
    """
    pass 
    def is_prime(n):
        n = int(input("type a number: "))
        if n < 1 and n / 2 != 0:
            print("Ture")
        else:
            print("Fales")
    is_prime(n)

    def factorial(n):
    """
    This function takes a number as input and returns its factorial.
    :param n: int
    :return: int, the factorial of the input number
    """
    pass 
    def factorial(number):
        total = 1
        for i in range(1,number+1):
            total *= i
        print(total)
    factorial(7)

def find_maximum(lst):
    """
    This function takes a list of numbers lst and returns the maximum number in the list.
    :param lst: list of int
    :return: int, the maximum number in the list
    """
    pass  
    lst = [3, 5, 6, 3, 6, 9, 189]
    def find_maxium(list):
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
    pass 
    def odd_or_even(n):
        n = int(input("type a number: "))
        if n / 2 == 0:
            print("even")
        else:
            print("odd")
    odd_or_even(n)

def is_palindrome(s):
    """
    This function takes a string `s` and returns `True` if the string is a palindrome, and `False` otherwise. 
    A palindrome is a word or phrase that reads the same backward as forward.
    
    :param s: str
    :return: bool, `True` if the string is a palindrome, `False` otherwise.
    """
    pass  
    def is_palindrome(s):
        ss=""
        for i in range(len(s)):
            ss=s[len(s)-i-1]
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
    pass  
    def find_gcd(a, b):
        if (a == 0):
        return b
         if (b == 0):
        return a
 
        if (a == b):
        return a
 
        if (a > b):
            return gcd(a-b, b)
        return gcd(a, b-a)
    
    a = 98
    b = 56
    if(gcd(a, b)):
        print('GCD of', a, 'and', b, 'is', gcd(a, b))
    else:
        print('not found')



