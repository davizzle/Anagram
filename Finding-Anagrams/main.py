# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

a = str(input("Enter a word: "))
b = str(input("Enter another word: "))

def find_anagram(word, anagram):
    # [assignment] Add your code here

    sortedWord = sorted(word)
    sortedAnagram = sorted(anagram)
    if sortedWord == sortedAnagram:
        return True
    
    else:
        return False

print(find_anagram(a, b))

