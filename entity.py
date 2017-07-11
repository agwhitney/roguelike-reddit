class Entity:
    """A generic object to represent players, enemies, items, etc.
    'Enemies, items, and whatever foreign entities we can dream of'
    """
    def __init__(self, x, y, char, color, name, blocks=False):
        self.x = x
        self.y = y
        self.char = char
        self.color = color
        self.name = name
        self.blocks = blocks

    def move(self, dx, dy):
        """Move the entity by a given amount."""
        self.x += dx
        self.y += dy


def get_blocking_entities_at_location(entities, destination_x, destination_y):
    """The function relates to entities (which puts it in this file), but it doesn't relate to
    a specific entity. Hence, it gets its own function separated from the Entity class.
    """
    for entity in entities:
        if entity.blocks and entity.x == destination_x and entity.y == destination_y:
            return entity
    return None
