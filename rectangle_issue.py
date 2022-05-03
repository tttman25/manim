
from manimlib import *


class Get_RiemannRectangle_issue(Scene):
    def construct(self):
        ax = Axes((-10, 10), (-10, 10))
        graph = ax.get_graph(lambda x: 0.5 * x ** 2)
        rect_left = ax.get_riemann_rectangles(graph, [1.0, 6.5], 0.5, "left", 1, BLACK)

        self.add(ax, graph, rect_left)
