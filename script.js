/**

Sentence Smash

Write a function that takes an array of words and smashes them together into a sentence and returns the sentence. You can ignore any need to sanitize words or add punctuation, but you should add spaces between each word. Be careful, there shouldn't be a space at the beginning or the end of the sentence!
Example
['hello', 'world', 'this', 'is', 'great']  =>  'hello world this is great'
 
 */   

function smash (words) {
   return words.join(' ').trim();
};

/**
 * 
 * PseudoCode:

This function will check wether a line is a Palindrome
Looping through it:
function PalindromeChecker(WordToCheck):
  
  for all letters.toString() in that word to check
      if letter at index  != letter at index negative index +1:
        return False 
     
   return true
        
        
or using inbuild methods and less code:
 
 
  if string == str(string).split("").reverse()
    return True
  else
    return False
    

*/

function isPalindrome(line) {
  if (line.toString() == line.toString().split("").reverse().join("")) {
    return true;
  }
return false;
}