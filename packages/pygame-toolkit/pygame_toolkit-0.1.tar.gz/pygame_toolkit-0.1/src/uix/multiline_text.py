import pygame as pg
from . import Container
from . import Text


class MultilineText(object):

    def __init__(
        self, text, size, font=[20, None], antialias=False,
        color=[0, 0, 0], background=None, shadow=(None, (0, 0)),
        orientation='vertical', alignment='center', spacement=2
    ):
        self.text = text
        self.size = size
        self.font = font
        self.antialias = antialias
        self.color = color
        self.background = background
        self.shadow = shadow
        self.orientation = orientation
        self.alignment = alignment
        self.spacement = spacement
        self.lines = []
        self.split_lines()
        self.container = Container(
            self.lines,
            self.orientation,
            self.alignment,
            self.spacement
        )

    def split_lines(self):
        lines = self.text.split('\n')
        text_args = {
            'font': self.font,
            'antialias': self.antialias,
            'color': self.color,
            'background': self.background,
            'shadow': self.shadow
        }
        max_width = self.size[0]

        for line in lines:
            words = line.split(' ')
            last_line = ''
            last_text = None

            for i, word in enumerate(words):
                current_line = f'{last_line}{word} '
                current_text = Text(current_line, **text_args)
                width = current_text.rect.width
                is_last_word = i == len(words) - 1

                if width > max_width and is_last_word:
                    if last_text != None:
                        self.lines.append(last_text)
                        current_text = Text(word, **text_args)
                        self.lines.append(current_text)
                    else:
                        self.lines.append(current_text)
                elif width > max_width and not(is_last_word):
                    if last_text != None:
                        self.lines.append(last_text)
                        last_line = f'{word} '
                        last_text = Text(word, **text_args)
                    else:
                        self.lines.apppend(current_text)
                        last_line = ''
                        last_text = None
                elif width <= max_width and is_last_word:
                    self.lines.append(current_text)
                elif width <= max_width and not(is_last_word):
                    last_line = current_line
                    last_text = current_text

    def draw(self, screen=None):
        if screen == None:
            screen = pg.display.get_surface()

        self.container.draw(screen)

    @property
    def rect(self):
        return self.container.rect
