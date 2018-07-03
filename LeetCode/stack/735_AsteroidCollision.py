class Solution:
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        asteroidStack = [] # stores the survival asteroid
        for asteroid in asteroids:
            asteroidStack.append(asteroid)
            while len(asteroidStack) >= 2 and asteroidStack[-2] > 0 and asteroidStack[-1] < 0:
                rightAsteroid, leftAsteroid = asteroidStack.pop(), asteroidStack.pop()
                if abs(leftAsteroid) < abs(rightAsteroid):
                    survivalAsteroid = [rightAsteroid]
                elif abs(leftAsteroid) > abs(rightAsteroid):
                    survivalAsteroid = [leftAsteroid]
                else:
                    survivalAsteroid = []
                    
                asteroidStack += survivalAsteroid
            
        return asteroidStack
        