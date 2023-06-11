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

function rockPaperScisors(p1,p2) {
  construct winn_list = [nameOfPlayers]
  construct play_list = [p1,p2]

  if for all cases (x,y are in play_list) {
    return full sentence "$'winn_list[play_list.indexOf(winner')"

  }
}
 
 
 */

const rps = (p1, p2) => {
  let winner_list = ["Player 1", "Player 2"]
  let play_list = [p1, p2]
  
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

/** 
 * Description:

Write a function that takes a list of strings as an argument and returns a filtered list containing the same elements but with the 'geese' removed.

The geese are any strings in the following array, which is pre-populated in your solution:

  ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]

For example, if this array were passed as an argument:

 ["Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse", "Blue Swedish"]

Your function would return the following array:

["Mallard", "Hook Bill", "Crested", "Blue Swedish"]

The elements in the returned array should be in the same order as in the initial array passed to your function, albeit with the 'geese' removed. Note that all of the strings will be in the same case as those provided, and some elements may be repeated.

 */

function gooseFilter (list) {
  let geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
  let new_list = []
  list.forEach((item)  => {
    if (!(geese.includes(item))){
      new_list.push(item)};
    });
   return new_list   
  }
  


  function gooseFilter (birds) {
    var geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"];
    return birds.filter(bird => !geese.includes(bird));
  };


freeGeese(["Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse", "Blue Swedish"])

