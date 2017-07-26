import libtcodpy as libtcod
from math import sqrt
from render_functions import RenderOrder


class Entity:
    """A generic object to represent players, enemies, items, etc.
    'Enemies, items, and whatever foreign entities we can dream of'
    """
    def __init__(self, x, y, char, color, name, blocks=False, render_order=RenderOrder,
                 fighter=None, ai=None, item=None, inventory=None):
        self.x = x
        self.y = y
        self.char = char
        self.color = color
        self.name = name
        self.blocks = blocks
        self.render_order = render_order
        # Components
        self.fighter = fighter
        self.ai = ai
        self.item = item
        self.inventory = inventory

        if self.fighter:
            self.fighter.owner = self

        if self.ai:
            self.ai.owner = self

        if self.item:
            self.item.owner = self

        if self.inventory:
            self.inventory.owner = self

    def move(self, dx, dy):
        """Move the entity by a given amount."""
        self.x += dx
        self.y += dy

    def move_towards(self, target_x, target_y, game_map, entities):
        dx = target_x - self.x
        dy = target_y - self.y
        distance = sqrt(dx**2 + dy**2)

        dx = int(round(dx / distance))
        dy = int(round(dy / distance))

        if not (game_map.is_blocked(self.x + dx, self.y + dy) or
                get_blocking_entities_at_location(entities, self.x + dx, self.y + dy)):
            self.move(dx, dy)

    def distance(self, x, y):
        return sqrt((x - self.x)**2 + (y - self.y)**2)

    def distance_to(self, other):
        dx = other.x - self.x
        dy = other.y - self.y
        return sqrt(dx**2 + dy**2)

    def move_astar(self, target, entities, game_map):
        """A* pathfinding algorithm to use with the AI"""
        # Create a FOV map with the dimensions of the map
        fov = libtcod.map_new(game_map.width, game_map.height)

        # Scan the current map each turn and set the walls as unwalkable
        for y1 in range(game_map.height):
            for x1 in range(game_map.width):
                libtcod.map_set_properties(fov, x1, y1, not game_map.tiles[x1][y1].block_sight,
                                           not game_map.tiles[x1][y1].solid)

        # Scan all the objects to see if some that should be navigated around
        # Check also that the object isn't self or the target (start and end points free)
        # The AI class handles the situation if self is next to the target, so it doesn't use A*
        for entity in entities:
            if entity.blocks and entity != self and entity != target:
                # Set the tile as a wall so that it must be navigated around (see above)
                libtcod.map_set_properties(fov, entity.x, entity.y, True, False)

        # Allocate an A* path - 1.41 is the normal diagonal cost of moving. Set to 0.0 if no diagonals.
        my_path = libtcod.path_new_using_map(fov, 1.41)

        # Compute the path between self and target's coordinates
        libtcod.path_compute(my_path, self.x, self.y, target.x, target.y)

        # Check if the path exists and (in this case) is less than 25 tiles
        # Path size matters if you want the monster to use a longer path, like through another room
        # But it should be relatively low so that monsters aren't running all over the place
        if not libtcod.path_is_empty(my_path) and libtcod.path_size(my_path) < 25:
            # Find the next coordinates in the computed full path
            x, y = libtcod.path_walk(my_path, True)
            if x or y:
                # Set self coordinates to next path tile
                self.x = x
                self.y = y
        else:
            # Keep the old move function as a backup so that if there are no paths (eg another monster in the way)
            # It will still try to move towards the player
            self.move_towards(target.x, target.y, game_map, entities)

        # Delete the path to free memory
        libtcod.path_delete(my_path)


def get_blocking_entities_at_location(entities, destination_x, destination_y):
    """The function relates to entities (which puts it in this file), but it doesn't relate to
    a specific entity. Hence, it gets its own function separated from the Entity class.
    """
    for entity in entities:
        if entity.blocks and entity.x == destination_x and entity.y == destination_y:
            return entity
    return None
