from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Approach 1: Simple Solution
        # 1. Create a dictionary 
        # 2. Sort the characters in the word, if the key doesn't exist, create a new entry. 
        #    Otherwise, append the word to the existing list.
        # 3. Return the list of grouped anagrams by extracting values from the dictionary.
        # _______________________________________________________________
        # Drawback: Sorting each word takes O(n log n), where n is the length of the word.
        # _______________________________________________________________
        # Space Complexity: O(n), where n is the total number of words in the input list.
        # Time Complexity: O(m * n log n), where m is the number of words and n is the length of the longest word.
        
        anagrams = {}

        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in anagrams:
                anagrams[sorted_word] = [word]
            else:
                anagrams[sorted_word].append(word)

        return list(anagrams.values())

        # Approach 2: Optimized solution 
        # 1. Instead of sorting, count the frequency of each letter in the word.
        # 2. Use the tuple of counts as the key in the dictionary. 
        # 3. Time complexity improves, counting letters in a word takes O(n) instead of O(n log n) for sorting.
        # _______________________________________________________________
        # Space Complexity: O(n)
        # Time Complexity: O(m * n), where m is the number of words and n is the length of the word.

        # TODO: Implement Approach 2