"""
Description:

Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.
Examples input/output:

XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false

MY SOLUTION """

def xo(s):
    if s:
        amount_x = 0
        amount_o = 0
        for i in s.lower():
            if i == 'x':
                amount_x += 1
            if i == 'o':
                amount_o += 1
        if amount_x == amount_o:
            return True
        else:
            return False
    else:
        return True
        
            
"""
Description:
The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.
What if the string is empty? Then the result should be empty object literal, {}.
"""

def count(s):
    dictionary = {}
    if not s:
        return dictionary
    else:
        for letter in s:
            if letter in dictionary:
                dictionary[letter] += 1
            else:
                dictionary[letter] = 1
        return dictionary      

"""
Description:
In this kata, your goal is to write a function which will reverse the vowels in a string. Any characters which are not vowels should remain in their original position. Here are some examples:
"Hello!" => "Holle!"
"Tomatoes" => "Temotaos"
"Reverse Vowels In A String" => "RivArsI Vewols en e Streng"
For simplicity, you can treat the letter y as a consonant, not a vowel.
"""



def reverse_vowels(s):
    string_list = list(s)
    both_list = [[i,letter] for i,letter in enumerate(string_list) if letter.lower() in ['a', 'e','i','o','u']]
    for item in both_list:
        string_list[item[0]] = both_list[-(both_list.index(item)+1)][1]
    return ''.join(string_list)


"""Description:

You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

Implement the function which takes an array containing the names of people that like an item. It must return the display text as shown in the examples:

[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"

Note: For 4 or more names, the number in "and 2 others" simply increases.
"""

def likes(names):
    if names:
        if len(names) == 1:
            return (f"{names[0]} likes this")
        elif len(names) == 2:
            return (f"{names[0]} and {names[1]} like this")
        elif len(names) == 3:
            return (f"{names[0]}, {names[1]} and {names[2]} like this")
        elif len(names) > 3:
            return(f"{names[0]}, {names[1]} and {len(names)-2} others like this")
    
    return "no one likes this"

    # Or a simple and great solution :

def likes_shorter(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: f'{names[0]} likes this',
        2: f'{names[0]} and {names[1]} like this',
        3: f'{names[0]}, {names[1]}, and {names[2]} like this',
        4: f'{names[0]}, {names[1]}, and {n-2} others like this'
    }[min(4, n)]

# or 

def likes(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this', 
        2: '{} and {} like this', 
        3: '{}, {} and {} like this', 
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)

"""
create a calculater function using leteral numbers and callback functions. This time we want to write calculations using functions and get the results. Let's have a look at some examples:

seven(times(five())) # must return 35


Requirements:

    There must be a function for each number from 0 ("zero") to 9 ("nine")
    There must be a function for each of the following mathematical operations: plus, minus, times, divided_by
    Each calculation consist of exactly one operation and two numbers
    The most outer function represents the left operand, the most inner function represents the right operand
    Division should be integer division. For example, this should return 2, not 2.666666...:

    
    What I have learned: 
    1.
    the concept of closure of functions!!! Basically: if I return an inner function I can asignt
    the outer function to a variable, when I then call the variable I can give parameters that will be used within the inner function.
    The variable will work as a functioncall for the inner function. This is because the scope and memory of the different functions in Python.
    2. 
    the concept of lambda. Lambda is a throwaway function that follows the syntax lambda x,y: x+y first part are the arguments, 
    second is what it returns...
"""



def zero(second_function = None):
    if second_function:
        return second_function(0)
    return 0

def one(second_function=None):
    if second_function:
        return second_function(1)
    return 1

def two(second_function=None):
    if second_function:
        return second_function(2)
    return 2
    
def three(second_function=None):
    if second_function:
        return second_function(3)
    return 3   

def four(second_function=None):
    if second_function:
        return second_function(4)
    return 4   

def five(second_function=None):
    if second_function:
        return second_function(5)
    return 5      

def six(second_function=None):
    if second_function:
        return second_function(6)
    return 6  

def seven(second_function=None):
    if second_function:
        return second_function(7)
    return 7

def eight(second_function=None):
    if second_function:
        return second_function(8)
    return 8

def nine(second_function=None):
    if second_function:
        return second_function(9)
    return 9



def plus(third_function):
    def inner_function(left_number):
        return left_number + third_function 
    return inner_function

def minus(third_function):
    def inner_function(left_number):
        return left_number - third_function 
    return inner_function

def times(third_function):
    def inner_function(left_number):
        return left_number * third_function 
    return inner_function

def divided_by(third_function):
    def inner_function(left_number):
        return left_number // third_function 
    return inner_function


