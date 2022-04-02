from manimlib import *


class Issue1Recreation(Scene):
    def construct(self):
        grid = NumberPlane()
        self.play(ShowCreation(grid))
        axes = Axes((-20, 20), (-20, 20))
        axes.add_coordinate_labels()

        self.play(Write(axes, lag_ratio=0.01, run_time=1))

        graph = axes.get_graph(
            lambda x: 1/x,
            discontinuities=[0],
            color=RED,
        )
        self.play(ShowCreation(graph))
