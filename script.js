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



/** an algo for rock, paper, scissors
 PseudoCode:
 
 
 */

const rps = (p1, p2) => {
  winner_list = ["Player 1", "Player 2"]
  play_list = [p1, p2]
  
  if (play_list.includes("scissors")&&play_list.includes("paper")){
      return `${winner_list[play_list.indexOf("scissors")]} won!`
      }
  else if (play_list.includes("scissors")&& play_list.includes("rock")){
      return `${winner_list[play_list.indexOf("rock")]} won!`
      }
  else if (play_list.includes("paper")&& play_list.includes("rock")){
      return `${winner_list[play_list.indexOf("paper")]} won!`    
      }
  else if (p1==p2){
      return "Draw!"
  }
};