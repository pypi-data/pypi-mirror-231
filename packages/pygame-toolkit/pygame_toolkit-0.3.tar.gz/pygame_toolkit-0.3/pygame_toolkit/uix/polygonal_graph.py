import pygame as pg
import math
from ..tools import font_loader


class PolygonalGraph():

    def __init__(
        self, values, max_radius, max_value=None, color=(0, 0, 0),
        thickness=5, show_labels=True, show_numbers=False, font=[40, None],
        labels_color=(0, 0, 0), spacement=1.1, screen=None
    ):
        if isinstance(values, dict):
            self.labels = values.keys()
            self.values = values.values()

            if show_numbers:
                self.labels = [
                    f'{label}: {value}' for label, value in values.items()
                ]
        else:
            self.values = values
            self.labels = None

        self.sides = len(self.values)
        self.max_value = max_value if max_value else max(self.values)
        self.max_radius = max_radius
        self.color = color
        self.thickness = thickness
        self.show_labels = show_labels
        self.show_numbers = show_numbers
        self.font = font_loader.load_font(font)
        self.labels_color = labels_color
        self.spacement = spacement
        self.screen = screen if screen else pg.display.get_surface()
        size = self.max_radius * 2 * (self.spacement + self.spacement - 1)
        self.rect = pg.Rect(0, 0, size, size)
        self.rect.center = self.screen.get_rect().center

        self.calculate()

    def calculate(self):
        self.radius = [
            self.calculate_radius(value) for value in self.values
        ]
        self.points, self.label_points = self.calculate_points()

    def calculate_radius(self, value):
        return (value / self.max_value) * self.max_radius

    def calculate_points(self):
        points = []
        label_points = []
        angle = (2 * math.pi) / self.sides
        start_angle = math.pi / 2 + math.pi

        for i in range(self.sides):
            current_angle = start_angle + (i * angle)

            point_x = self.rect.centerx + math.cos(current_angle) \
                * self.radius[i]
            point_y = self.rect.centery + math.sin(current_angle) \
                * self.radius[i]
            points.append((point_x, point_y))

            label_x = self.rect.centerx + math.cos(current_angle) * \
                (self.max_radius * self.spacement)
            label_y = self.rect.centery + math.sin(current_angle) * \
                (self.max_radius * self.spacement)
            label_points.append((label_x, label_y))

        return points, label_points

    def draw(self):
        if self.labels and self.show_labels:
            self.draw_labels()

        self.draw_polygon()

    def draw_polygon(self):
        pg.draw.polygon(
            self.screen, self.color, self.points, self.thickness
        )

    def draw_labels(self):
        for label, point in zip(self.labels, self.label_points):
            text = self.font.render(
                label, True, self.labels_color
            )
            text_rect = text.get_rect(center=point)
            self.screen.blit(text, text_rect)

