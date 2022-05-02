from manimlib import *

class Issue1Recreation(Scene):
    def construct(self):
        group_0 = Tex("A").replicate(3).arrange(RIGHT).shift(UP)
        group_1 = Circle().replicate(2).arrange(RIGHT).shift(DOWN)
        self.add(group_0)
        self.play(FadeTransformPieces(group_0, group_1), run_time=3)
        self.wait()


class Issue2Recreation(Scene):
    def construct(self):
        mob = Dot()
        # mob = Line().set_color([BLUE, RED])
        # mob = Line().set_opacity(opacity=[0, 1])

        dot = FillArrow()
        self.add(mob)
        self.wait()
        self.play(Transform(mob, dot))
        self.wait()