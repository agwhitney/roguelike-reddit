import libtcodpy as libtcod
from random import randint
from entity import Entity
from map_objects.tile import Tile
from map_objects.rectangle import Rect
from components.fighter import Fighter
from components.ai import BasicMonster
from components.item import Item
from render_functions import RenderOrder


class GameMap:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = self.initialize_tiles()

    def initialize_tiles(self):
        """Initialize solid tiles based on the map size; rooms/tunnels are 'carved' out of this."""
        tiles = [[Tile(True) for y in range(self.height)] for x in range(self.width)]
        return tiles

    def make_map(self, max_rooms, room_min_size, room_max_size, map_width, map_height,
                 player, entities, max_monsters_per_room, max_items_per_room):
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

                # Place entities into the room
                self.place_entities(new_room, entities, max_monsters_per_room, max_items_per_room)

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

    @staticmethod
    def place_entities(room, entities, max_monsters_per_room, max_items_per_room):
        """Places monsters and items in the room"""
        number_of_monsters = randint(0, max_monsters_per_room)
        number_of_items = randint(0, max_items_per_room)

        for i in range(number_of_monsters):
            # Random location in the room
            x = randint(room.x1 + 1, room.x2 - 1)
            y = randint(room.y1 + 1, room.y2 - 1)

            # 80% orc, 20% troll. Makes sure there are no entities already at the position
            if not any([entity for entity in entities if entity.x == x and entity.y == y]):
                if randint(0, 100) < 80:
                    fighter_component = Fighter(hp=10, defense=0, power=3)
                    ai_component = BasicMonster()

                    monster = Entity(x, y, 'o', libtcod.desaturated_green, 'Orc', blocks=True,
                                     render_order=RenderOrder.ACTOR, fighter=fighter_component, ai=ai_component)
                else:
                    fighter_component = Fighter(hp=16, defense=1, power=4)
                    ai_component = BasicMonster()

                    monster = Entity(x, y, 'T', libtcod.darker_green, 'Troll', blocks=True,
                                     render_order=RenderOrder.ACTOR, fighter=fighter_component, ai=ai_component)

                entities.append(monster)

        for i in range(number_of_items):
            x = randint(room.x1 + 1, room.x2 - 1)
            y = randint(room.y1 + 1, room.y2 - 1)

            if not any([entity for entity in entities if entity.x == x and entity.y == y]):
                item_component = Item()
                item = Entity(x, y, '!', libtcod.violet, 'Healing Potion', render_order=RenderOrder.ITEM,
                              item=item_component)

                entities.append(item)

    def is_blocked(self, x, y):
        if self.tiles[x][y].solid:
            return True
        return False
