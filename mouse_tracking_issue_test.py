from manimlib import *


class MouseTrackingRecreation(Scene):
    def construct(self):
        cursor_dot = Dot()
        cursor_dot.add_updater(lambda dot, dt: dot.move_to(self.mouse_point))
        self.play(Write(cursor_dot))
