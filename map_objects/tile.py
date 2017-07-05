class Tile:
    """
    A tile on a map. It may or may not be solid,
    and may or may not block sight.

    'solid' is changed from 'blocked' in the tutorial
    """
    def __init__(self, solid, block_sight=None):
        self.solid = solid

        # By default, a blocked tile blocks sight
        if block_sight is None:
            block_sight = solid   # Changing the passed var, not the attribute
        self.block_sight = block_sight
