import sys
import pygame as pg
from .tools import font_loader


class FpsDisplay():

    def __init__(
        self, clock, foreground, background, antialias, font, position,
        precision
    ):
        self.clock = clock
        self.foreground = foreground
        self.background = background
        self.antialias = antialias
        self.font = font_loader.load_font(font)
        self.position = position
        self.precision = precision
        self.visible = True

    def draw(self, screen=None):
        if self.visible:
            if screen == None:
                screen = pg.display.get_surface()

            fps_value = self.clock.get_fps()
            fps_text = f'FPS: {fps_value:.{self.precision}f}'
            fps_surf = self.font.render(
                fps_text, self.antialias, self.foreground, self.background
            )
            fps_rect = fps_surf.get_rect()
            position_value = getattr(screen.get_rect(), self.position)
            setattr(fps_rect, self.position, position_value)

            screen.blit(fps_surf, fps_rect)


class ScheduledEvent():

    def __init__(self, core, repeat, interval, function, *args, **kwargs):
        self.core = core
        self.repeat = repeat
        self.start = pg.time.get_ticks()
        self.interval = interval
        self.function = lambda: function(*args, **kwargs)

    @property
    def target_time_reached(self):
        return pg.time.get_ticks() >= self.start + self.interval

    def call_function(self):
        if self.target_time_reached:
            self.function()

            if self.repeat:
                self.start = pg.time.get_ticks()
            else:
                self.quit()

    def quit(self):
        self.core.scheduled_events.remove(self)


class Core():

    def __init__(
        self, size=(0, 0), flags=pg.FULLSCREEN | pg.SRCALPHA,
        fps_foreground=(255, 255, 0), fps_background=(0, 0, 0),
        fps_antialias=False, fps_font=[20, None], fps_position='topright',
        fps_precision=1
    ):
        pg.init()

        self.screen = pg.display.set_mode(size, flags)
        self.screen_rect = self.screen.get_rect()
        self.screen_color = (255, 255, 255)
        self.clock = pg.time.Clock()
        self.max_fps = 0
        self.fps_display = FpsDisplay(
            self.clock, fps_foreground, fps_background, fps_antialias,
            fps_font, fps_position, fps_precision
        )
        self.scheduled_events = []
        self.quit_keys = [27]  # 27 = Esc
        self.running = True

    def run(self):
        while self.running:
            self._check_scheduled_events()
            self._check_quit_event()
            self.update()
            self._draw()
            self.clock.tick(self.max_fps)

    def _check_scheduled_events(self):
        for event in self.scheduled_events:
            event.call_function()

    def _check_quit_event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or event.type == pg.KEYDOWN \
                    and event.key in self.quit_keys:
                self.exit()
                sys.exit()

    def exit(self):
        pass

    def update(self):
        pass

    def _draw(self):
        self.screen.fill(self.screen_color)
        self.draw()
        self.fps_display.draw()
        pg.display.flip()

    def draw(self):
        pass

    def set_interval(self, interval, function, *args, **kwargs):
        event = ScheduledEvent(
            self, True, interval, function, *args, **kwargs
        )

        self.scheduled_events.append(event)

        return event

    def set_timeout(self, interval, function, *args, **kwargs):
        event = ScheduledEvent(
            self, False, interval, function, *args, **kwargs
        )

        self.scheduled_events.append(event)

        return event
