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
        
            
            
            