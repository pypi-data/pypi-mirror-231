import pygame as pg

class Container():

    def __init__(
        self, elements, orientation='vertical', alignment='center', spacement=0
    ):
        self.elements = elements
        self.orientation = orientation
        self.alignment = alignment
        self.spacement = spacement

        widths = [
            element.rect.width + self.spacement for element in self.elements
        ]
        heights = [
            element.rect.height + self.spacement for element in self.elements
        ]
        width = sum(widths) - self.spacement if self.orientation == 'horizontal' \
            else max(widths) - self.spacement
        height = sum(heights) - self.spacement if self.orientation == 'vertical' \
            else max(heights) - self.spacement

        self._rect = pg.Rect(0, 0, width, height)
        self.rect_accessed_times = 0

        self.update()

    @property
    def rect(self):
        self.rect_accessed_times += 1
        return self._rect

    def update(self):
        if self.orientation == 'vertical':
            top = self._rect.top

            if self.alignment == 'center':
                for element in self.elements:
                    element.rect.midtop = (
                        self._rect.centerx, top
                    )
                    top += element.rect.height + self.spacement
            elif self.alignment == 'left':
                for element in self.elements:
                    element.rect.topleft = (
                        self._rect.left, top
                    )
                    top += element.rect.height + self.spacement
            elif self.alignment == 'right':
                for element in self.elements:
                    element.rect.topright = (
                        self.rect.right, top
                    )
                    top += element.rect.height + self.spacement
        elif self.orientation == 'horizontal':
            left = self.rect.left

            if self.alignment == 'center':
                for element in self.elements:
                    element.rect.midleft = (
                        left, self._rect.centery
                    )
                    left += element.rect.width + self.spacement
            elif self.alignment == 'top':
                for element in self.elements:
                    element.rect.topleft = (
                        left, self._rect.top
                    )
                    left += element.rect.width + self.spacement
            elif self.alignment == 'bottom':
                for element in self.elements:
                    element.rect.bottomleft = (
                        left, self._rect.bottom
                    )
                    left += element.rect.width + self.spacement

    def draw(self, screen=None):
        if self.rect_accessed_times > 0:
            # Updates only when needed but it is still automatical
            self.update()

        if screen == None:
            screen = pg.display.get_surface()

        for element in self.elements:
            element.draw(screen)

        self.rect_accessed_times = 0
