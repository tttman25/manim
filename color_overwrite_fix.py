from manimlib import *


class Code1623(Scene):
    def construct(self):
        num = DecimalNumber(0, color=ORANGE).scale(2)
        self.add(num)
        self.play(num.animate.set_value(2))