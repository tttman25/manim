from manimlib import *

class Issue1Recreation(Scene):
    def construct(self):
        group_0 = Tex("A").replicate(3).arrange(RIGHT).shift(UP)
        group_1 = Circle().replicate(2).arrange(RIGHT).shift(DOWN)
        self.add(group_0)
        self.play(FadeTransformPieces(group_0, group_1), run_time=3)
        self.wait()