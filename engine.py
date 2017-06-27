import libtcodpy as libtcod
import input_handlers as inputs


def main():
    SCREEN_WIDTH = 80
    SCREEN_HEIGHT = 50

    player_x = int(SCREEN_WIDTH / 2)
    player_y = int(SCREEN_HEIGHT / 2)

    libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
    libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'libtcod tutorial revised', False)

    con = libtcod.console_new(SCREEN_WIDTH, SCREEN_HEIGHT)

    key = libtcod.Key()
    mouse = libtcod.Mouse()

    while not libtcod.console_is_window_closed():
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)

        libtcod.console_set_default_foreground(con, libtcod.white)  # Color of character on foreground in window 0
        libtcod.console_put_char(con, player_x, player_y, '@', libtcod.BKGND_NONE)  # Places the character (@)
        libtcod.console_blit(con, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0, 0)
        libtcod.console_flush()     # Presents everything on the screen

        libtcod.console_put_char(con, player_x, player_y, ' ', libtcod.BKGND_NONE)  # Replaces @ when it moves

        action = inputs.handle_keys(key)

        move = action.get('move')
        exit = action.get('exit')
        fullscreen = action.get('fullscreen')

        if move:
            dx, dy = move
            player_x += dx
            player_y += dy
        if exit:
            return True
        if fullscreen:
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())


if __name__ == '__main__':
    main()
