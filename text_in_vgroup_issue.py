from manimlib import *


class VGroupAnimationRecreation(Scene):
    def construct(self):
        t1 = Text("A", color=BLUE)
        t2 = Text("B", color=YELLOW)
        t3 = Text("C", color=RED)
        t4 = Text("D", color=BLACK)
        t = VGroup(t1, t2, t3, t4).arrange(RIGHT).scale(2)
        self.play(Write(t))
        self.wait()
