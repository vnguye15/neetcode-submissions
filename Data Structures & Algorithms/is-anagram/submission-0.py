class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        countS = defaultdict(int)
        countT = defaultdict(int)

        for i in range(len(s)):
            countS[s[i]] += 1 # + countT.get(t[i], 0) --> if defaultdict(int) wasn't there
            # Updating the amount of occurences for the character, get 
            # ex: for a, the first time 
            countT[t[i]] += 1 # + countT.get(t[i], 0) --> if defaultdict(int) wasn't there

        return countS == countT

# for c in countS:
        #     if countS[c] != countT.get(c, 0):
        #         return False
        # return True

#Understand:
# Every word with same characters is considered an anagram
# racecar vs carrace, jar vs jam 
# dealing with 2 strings --> s & t 
# Input: string | Output: boolean 
# Anagram conditions: 1. Same Length, 2. Exact same characters 

# Plan
# First create two frequency hash maps (dictionaries)
# Check if each string is equal in length to each other
# From there, 


# Constraints: 
# * Convert both strings to lowercase (avoids incorrect comparison due to spelling)