from manimlib import *


class Test(Scene):
    def construct(self):
        SCALE = 3
        plane = NumberPlane((-2, 2), (-2, 2)).scale(SCALE)
        plane.set_stroke(BLUE_E, 1)

        self.add(plane)

        p1 = Point(plane.c2p(1, 0))
        line = Line(plane.get_origin(), p1.get_location()).set_stroke(GREEN_E, 2)
        # brace = always_redraw(Brace, line, UP)

        distance = DecimalNumber(0, num_decimal_places=2)
        # distance.next_to(line, UP)

        always(distance.next_to, p1, UP)
        # f_always(distance.set_value, lambda: line.get_length() / SCALE)
        # f_always(brace.rotate, line.get_angle)

        self.add(distance)
        # self.add(brace)

        self.play(
            ShowCreation(line)
        )

        for x in range(360//15):
            self.play(
                line.animate.set_angle(line.get_angle() + 15 * DEGREES)
            )
            self.wait(0.5)
