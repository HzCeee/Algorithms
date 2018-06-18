class Solution:
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        minPrice = [float('inf')]
        
        # return the minimal price to meet curNeeds after already paid curPrice
        # Note: update minPrice during DFS
        def shoppingOffersHelper(curPrice, curNeeds):
            for offer in special:
                if all(map(lambda x, y: x <= y, offer[:-1], curNeeds)):
                    minPossiblePrice = shoppingOffersHelper(
                        curPrice + offer[-1], 
                        list(map(lambda x, y: x - y, curNeeds, offer[:-1]))
                    )
                    minPrice[0] = min(minPrice[0], minPossiblePrice)
            
            for index, need in enumerate(curNeeds):
                if need > 0: curPrice += price[index] * need
            
            return min(minPrice[0], curPrice)
        
        return shoppingOffersHelper(0, needs)   