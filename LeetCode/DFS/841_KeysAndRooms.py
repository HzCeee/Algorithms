class Solution:
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        # return True if we can enter every locked rooms
        def canVisitAllRoomsHelper(curRoom, curKeys, visitedRooms):
            visitedRooms.add(curRoom)
            
            if len(visitedRooms) == len(rooms): return True
            
            for room in curKeys:
                if room in visitedRooms: continue
                if canVisitAllRoomsHelper(room, curKeys.union(set(rooms[room])), visitedRooms):
                    return True
            
            return False
        
        curRoom = 0
        curKeys = set(rooms[curRoom])
        visitedRooms = set()
        return canVisitAllRoomsHelper(curRoom, curKeys, visitedRooms)