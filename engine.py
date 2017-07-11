import libtcodpy as libtcod
from input_handlers import handle_keys
from entity import Entity, get_blocking_entities_at_location
from render_functions import clear_all, render_all
from map_objects.game_map import GameMap
from config_files.config import settings
from fov_functions import initialize_fov, recompute_fov
from game_states import GameStates


def main():
    # Screen, Map, FOV settings; Colors

    screen_width = settings['screen']['width']
    screen_height = settings['screen']['height']
    map_width = settings['map']['width']
    map_height = settings['map']['height']

    room_max_size = settings['room']['max_size']
    room_min_size = settings['room']['min_size']
    max_rooms = settings['room']['max_number']

    fov_algorithm = settings['fov']['algorithm']    # Default 0, has others to try!
    fov_light_walls = settings['fov']['light_walls']    # Light up walls or not
    fov_radius = settings['fov']['radius']

    max_monsters_per_room = settings['monsters']['max_per_room']

    colors = {
        'dark_wall': libtcod.Color(0, 0, 100),
        'dark_ground': libtcod.Color(50, 50, 150),
        'light_wall': libtcod.Color(130, 110, 50),
        'light_ground': libtcod.Color(200, 180, 50)
    }

    # Entity objects

    player = Entity(0, 0, '@', libtcod.white, 'Player', blocks=True)
    entities = [player]

    # Console, Map, and FOV initialization

    libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
    libtcod.console_init_root(screen_width, screen_height, 'libtcod tutorial revised', False)

    con = libtcod.console_new(screen_width, screen_height)
    game_map = GameMap(map_width, map_height)
    game_map.make_map(max_rooms, room_min_size, room_max_size, map_width, map_height,
                      player, entities, max_monsters_per_room)

    fov_recompute = True    # Only need to recompute when we move (and start!)
    fov_map = initialize_fov(game_map)  # Variable that is the fov result

    # Input variables and game state

    key = libtcod.Key()
    mouse = libtcod.Mouse()

    game_state = GameStates.PLAYERS_TURN

    while not libtcod.console_is_window_closed():
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)

        if fov_recompute:
            recompute_fov(fov_map, player.x, player.y, fov_radius, fov_light_walls, fov_algorithm)

        render_all(con, entities, game_map, fov_map, fov_recompute, screen_width, screen_height, colors)
        fov_recompute = False
        libtcod.console_flush()     # Presents everything on the screen
        clear_all(con, entities)    # Erases the old positions

        action = handle_keys(key)

        move = action.get('move')
        exit = action.get('exit')
        fullscreen = action.get('fullscreen')

        if move and game_state == GameStates.PLAYERS_TURN:
            dx, dy = move
            destination_x = player.x + dx
            destination_y = player.y + dy
            if not game_map.is_blocked(destination_x, destination_y):
                target = get_blocking_entities_at_location(entities, destination_x, destination_y)
                if target:
                    print("You kick the {}'s shinguard. 'Take that, rapscallion!'".format(entity.name))
                else:
                    player.move(dx, dy)
                    fov_recompute = True
            game_state = GameStates.ENEMY_TURN

        if exit:
            return True

        if fullscreen:
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())

        if game_state == GameStates.ENEMY_TURN:
            for entity in entities:
                if entity != player:
                    print("The {} doesn't NEED two balls.".format(entity.name))
            game_state = GameStates.PLAYERS_TURN


if __name__ == '__main__':
    main()
