import pygame as pg
from ..tools import font_loader


class Text():

    def __init__(
        self, text, font=[20, None], antialias=False, color=[0, 0, 0],
        background=None, shadow=(None, (0, 0))
    ):
        self.text = str(text)
        self.font = font_loader.load_font(font)
        self.antialias = antialias
        self.color = color
        self.background = background
        self.shadow = shadow

        self.render()

    def render(self):
        self.surf = self.font.render(
            self.text, self.antialias, self.color, self.background
        )
        self.rect = self.surf.get_rect()

        if self.shadow[0]:
            self.shadow_surf = self.font.render(
                self.text, self.antialias, self.shadow[0], self.background
            )

    def draw(self, screen=None):
        if screen == None:
            screen = pg.display.get_surface()

        if self.shadow[0]:
            screen.blit(self.shadow_surf, self.shadow_rect)

        screen.blit(self.surf, self.rect)

    @property
    def shadow_rect(self):
        return self.rect.move(self.shadow[1:])
