from manimlib import *


class Issue1Recreation(Scene):

    def construct(self):
        axes = ThreeDAxes()
        self.add(axes)
        #axes.to_corner(DOWN)
        axes.to_edge(DOWN)
