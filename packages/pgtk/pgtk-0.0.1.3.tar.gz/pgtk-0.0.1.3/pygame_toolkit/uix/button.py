import pygame as pg
from . import Text


class Button():

    def __init__(
        self, text, font=[20, None], antialias=True, text_color=[0, 0, 0],
        text_shadow=(None, (0, 0)), background=(150, 150, 150),
        shadow=(None, (0, 0)), border=(None, (0, 0)), border_radius=0,
        padding=(0, 0), width=0, height=0, background_hover=None
    ):
        self.text = Text(
            text, font, antialias, text_color, background, text_shadow
        )
        self.text_hover = Text(
            text, font, antialias, text_color, background_hover, text_shadow
        )
        self.background = background
        self.shadow = shadow
        self.border = border
        self.border_radius = border_radius
        width = width if width else self.text.rect.w + padding[0] * 2
        height = height if height else self.text.rect.h + padding[1] * 2
        self.inner_rect = pg.Rect(0, 0, width, height)
        self.border_rect = pg.Rect(
            0, 0, width + border[1][0], height + border[1][1]
        )
        self.background_hover = background_hover if background_hover != None \
            else self.background

    @property
    def rect(self):
        return self.border_rect

    def draw(self, screen=None):
        self.update()

        if screen == None:
            screen = pg.display.get_surface()

        is_mouse_hover = self.rect.collidepoint(pg.mouse.get_pos())

        background = self.background_hover if is_mouse_hover \
            else self.background

        if self.shadow[0] and not(is_mouse_hover):
            pg.draw.rect(
                screen, self.shadow[0], self.border_rect.move(self.shadow[1]),
                0, self.border_radius
            )

        if self.border[0]:
            pg.draw.rect(
                screen, self.border[0], self.border_rect, 0, self.border_radius
            )

        pg.draw.rect(
            screen, background, self.inner_rect, 0, self.border_radius
        )
        self.text.draw(screen)

    def update(self):
        self.inner_rect.center = self.border_rect.center
        self.text.rect.center = self.border_rect.center
