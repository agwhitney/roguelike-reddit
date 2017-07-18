import libtcodpy as libtcod
import textwrap


class Message:
    def __init__(self, text, color=libtcod.white):
        self.text = text
        self.color = color


class MessageLog:
    def __init__(self, x, width, height):
        self.messages = []
        self.x = x
        self.width = width
        self.height = height

    def add_message(self, message):
        """Adds a message to the message log and formats to width if necessary"""
        new_msg_lines = textwrap.wrap(message.text, self.width)

        for line in new_msg_lines:
            # If buffer is full, remove the first line to make room for the new one
            if len(self.messages) == self.height:
                del self.messages[0]

            self.messages.append(message)