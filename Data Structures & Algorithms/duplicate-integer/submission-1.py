class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        #Creating set named hashSet to store numbers
        hashset = set()
        for index in nums:
            # if the number ism't already contained in hash Set
            if index not in hashset:

                #add it to hashset
                hashset.add(index)
            else:
                #if it already is then return True
                return True
        #Return false if no duplicates found
        return False    