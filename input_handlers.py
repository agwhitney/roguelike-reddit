"""Handles keyboard inputs and returns them as a 'string: result' dictionary.
Hence the result can be gathered in engine.py via handle_keys.get(string).
Result is typically just True and handled by the engine.

Different functions handle different game states. Keep an empty dict catch for no input or you'll crash!
"""
import libtcodpy as libtcod
from game_states import GameStates


def handle_mouse(mouse):
    (x, y) = (mouse.cx, mouse.cy)

    if mouse.lbutton_pressed:
        return {'left_click': (x, y)}
    elif mouse.rbutton_pressed:
        return {'right_click': (x, y)}

    return {}


def handle_main_menu(key):
    key_char = chr(key.c)

    if key_char == 'a':
        return {'new_game': True}
    elif key_char == 'b':
        return {'load_game': True}
    elif key_char == 'c' or key.vk == libtcod.KEY_ESCAPE:
        return {'exit': True}

    return {}


def handle_keys(key, game_state):
    if game_state == GameStates.PLAYERS_TURN:
        return handle_player_turn_keys(key)

    elif game_state == GameStates.PLAYER_DEAD:
        return handle_player_dead_keys(key)

    elif game_state in (GameStates.SHOW_INVENTORY, GameStates.DROP_INVENTORY):
        return handle_inventory_keys(key)

    elif game_state == GameStates.TARGETING:
        return handle_targeting_keys(key)

    return {}


def handle_player_turn_keys(key):
    key_char = chr(key.c)   # Gets the character pressed on the keyboard

    # Movement Keys - now utilizing 'vim keys' for 8-directional movement
    if key.vk == libtcod.KEY_UP or key_char == 'k':
        return {'move': (0, -1)}
    elif key.vk == libtcod.KEY_DOWN or key_char == 'j':
        return {'move': (0, 1)}
    elif key.vk == libtcod.KEY_LEFT or key_char == 'h':
        return {'move': (-1, 0)}
    elif key.vk == libtcod.KEY_RIGHT or key_char == 'l':
        return {'move': (1, 0)}
    elif key_char == 'y':
        return {'move': (-1, -1)}
    elif key_char == 'u':
        return {'move': (1, -1)}
    elif key_char == 'b':
        return {'move': (-1, 1)}
    elif key_char == 'n':
        return {'move': (1, 1)}

    # Pick up item
    if key_char == 'g':
        return {'pickup': True}

    # Drop item
    if key_char == 'd':
        return {'drop_inventory': True}

    # Inventory Menu
    if key_char == 'i':
        return {'show_inventory': True}

    # Toggle fullscreen
    if key.vk == libtcod.KEY_ENTER and key.lalt:
        return {'fullscreen': True}

    # Exit the game
    elif key.vk == libtcod.KEY_ESCAPE:
        return {'exit': True}

    # No key pressed
    return {}


def handle_player_dead_keys(key):
    key_char = chr(key.c)

    # Inventory
    if key_char == 'i':
        return {'show_inventory': True}

    # Fullscreen
    if key.vk == libtcod.KEY_ENTER and key.lalt:
        return {'fullscreen': True}
    # Exit
    elif key.vk == libtcod.KEY_ESCAPE:
        return {'exit': True}

    return {}


def handle_inventory_keys(key):
    index = key.c - ord('a')

    if index >= 0:
        return {'inventory_index': index}

    if key.vk == libtcod.KEY_ENTER and key.lalt:
        return {'fullscreen': True}
    elif key.vk == libtcod.KEY_ESCAPE:
        return {'exit': True}

    return {}


def handle_targeting_keys(key):
    if key.vk == libtcod.KEY_ESCAPE:
        return {'exit': True}

    return {}
