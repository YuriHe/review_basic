class Solution:
    """
    Question: check if can open all lock rooms
    1.room[0] is unlock, can always get key in this room
    2.grap the key and open next room
    {curRoom: [k1, k2]}
    eg.(0:[1], 1:[2], 2:[3], 3: [])
       {0:[1,3], 1:[3,0,1], 2:[], 3: [0]}
    visitset store key is used
    keep in loop until no unlock rooom
    """
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # SOLUTION 1 LOOP
        if not rooms: return False

        visited_room = set()
        unlock_room = set()
        unlock_room.add(0) # add index 0

        while len(unlock_room) > 0:
            last = unlock_room.pop()
            visited_room.add(last)
            # grap keys
            keys = rooms[last]
            for key in keys:
                if key in visited_room:
                    continue
                else:
                    unlock_room.add(key)
        return len(visited_room) == len(rooms)

        # SOLUTION 2 dfs
        if not rooms: return False
        visited = set()
        def dfs(room):
            # NO NEED!
            # if not room:
            #     return
            # update
            visited.add(room)
            keys = rooms[room]
            for key in keys:
                if key not in visited:
                    dfs(key)

        # start 0 room
        dfs(0)
        print(visited)
        return len(visited) == len(rooms)