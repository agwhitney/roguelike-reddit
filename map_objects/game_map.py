from map_objects.tile import Tile
from map_objects.rectangle import Rect
from random import randint


class GameMap:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = self.initialize_tiles()

    def initialize_tiles(self):
        """Initialize solid tiles based on the map size; rooms/tunnels are 'carved' out of this."""
        tiles = [[Tile(True) for y in range(self.height)] for x in range(self.width)]
        return tiles

    def make_map(self, max_rooms, room_min_size, room_max_size, map_width, map_height, player):
        """Randomly generates rooms and tunnels between them based on the map dimensions,
        and also sets the player's position to be the center of the first room.
        """
        rooms = []      # List of room objects
        num_rooms = 0

        for r in range(max_rooms):
            # random width and height
            w = randint(room_min_size, room_max_size)
            h = randint(room_min_size, room_max_size)
            # random position without leaving the map boundaries
            x = randint(0, map_width - w - 1)
            y = randint(0, map_height - h - 1)

            # 'Rect' class makes rectangles easier to work with
            new_room = Rect(x, y, w, h)

            # go through other rooms and check if they intersect
            for other_room in rooms:
                if new_room.intersect(other_room):
                    break
            else:   # Python for-else: the else runs if for doesn't break!
                # No intersections: room is valid - so actually create it!
                self.create_room(new_room)
                # center coordinates of new room, for later
                new_x, new_y = new_room.center()
                if num_rooms == 0:
                    # This is the first room, where the player starts
                    player.x = new_x
                    player.y = new_y
                else:
                    # all rooms after the first: connect to previous with a tunnel
                    prev_x, prev_y = rooms[num_rooms - 1].center()
                    # flip a coin on moving horiz then vert, or vert then horiz
                    if randint(0, 1) == 1:
                        self.create_h_tunnel(prev_x, new_x, prev_y)
                        self.create_v_tunnel(prev_y, new_y, new_x)
                    else:
                        self.create_v_tunnel(prev_y, new_y, prev_x)
                        self.create_h_tunnel(prev_x, new_x, new_y)
                # finally, append the new room to the list
                rooms.append(new_room)
                num_rooms += 1

    def create_room(self, room):
        """Makes the tile objects in a room (rectangle object) passable, like a real room."""
        for x in range(room.x1 + 1, room.x2):   # + 1 guarantees a wall between two rooms
            for y in range(room.y1 + 1, room.y2):
                self.tiles[x][y].solid = False
                self.tiles[x][y].block_sight = False

    def create_h_tunnel(self, x1, x2, y):
        for x in range(min(x1, x2), max(x1, x2) + 1):
            self.tiles[x][y].solid = False
            self.tiles[x][y].block_sight = False

    def create_v_tunnel(self, y1, y2, x):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            self.tiles[x][y].solid = False
            self.tiles[x][y].block_sight = False

    def is_blocked(self, x, y):
        if self.tiles[x][y].solid:
            return True
        return False
