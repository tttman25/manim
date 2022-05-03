from manimlib import *


class get_3D_axis(ThreeDScene):
    def construct(self):
        ax = ThreeDAxes()
        self.set_camera_mob(phi=2 * PI / 5, theta=PI / 5)
        self.add(ax)

    def set_camera_mob(self, phi, theta):
        pass

