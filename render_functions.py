import libtcodpy as libtcod


def render_all(con, entities, game_map, screen_width, screen_height, colors):
    """Renders the game objects (map, entities) according to passed screen size and colors"""
    # Draw the map and color code walls from dictionary 'colors'
    for y in range(game_map.height):
        for x in range(game_map.width):
            wall = game_map.tiles[x][y].block_sight     # Boolean
            if wall:
                libtcod.console_set_char_background(con, x, y, colors.get('dark_wall'), libtcod.BKGND_SET)
            else:
                libtcod.console_set_char_background(con, x, y, colors.get('dark_ground'), libtcod.BKGND_SET)

    # Draw all entity objects in the 'entities' list
    for entity in entities:
        draw_entity(con, entity)

    libtcod.console_blit(con, 0, 0, screen_width, screen_height, 0, 0, 0)


def clear_all(con, entities):
    """Clear all entities in the console window"""
    for entity in entities:
        clear_entity(con, entity)


def draw_entity(con, entity):
    """Place an entity on the console window."""
    libtcod.console_set_default_foreground(con, entity.color)
    libtcod.console_put_char(con, entity.x, entity.y, entity.char, libtcod.BKGND_NONE)


def clear_entity(con, entity):
    """Erase the character representing the object by simply replacing it with a blank character."""
    libtcod.console_put_char(con, entity.x, entity.y, ' ', libtcod.BKGND_NONE)
