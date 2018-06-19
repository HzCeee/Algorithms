class Solution:
    def loudAndRich(self, richer, quiet):
        """
        :type richer: List[List[int]]
        :type quiet: List[int]
        :rtype: List[int]
        """
        richerRelation = {}
        for pair in richer:
            richerPerson, poorerPerson = pair
            if poorerPerson not in richerRelation:
                richerRelation[poorerPerson] = []
            richerRelation[poorerPerson].append(richerPerson)
        
        memo = {}
        
        # return the louder and richer person
        def loudAndRichHelper(person):
            if person in memo: return memo[person]
            
            if person not in richerRelation: 
                memo[person] = person
                return person
            
            ansPerson = person
            for richerPerson in richerRelation[person]:
                minQuietPerson = loudAndRichHelper(richerPerson)
                if quiet[minQuietPerson] < quiet[ansPerson]:
                    ansPerson = minQuietPerson
            
            memo[person] = ansPerson
            
            return ansPerson
        
        ans = [loudAndRichHelper(i) for i in range(len(quiet))]
        return ans
        
        