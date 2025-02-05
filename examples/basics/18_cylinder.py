import os
import math
from payton.scene import Scene
from payton.scene.geometry import Cylinder


def rotate(name, scene, period, total):
    scene.objects["cylinder"].rotate_around_z(math.radians(1))


scene = Scene()
cyl = Cylinder(height=2.0)

scene.create_clock("rotate", 0.01, rotate)

texture_file = os.path.join(os.path.dirname(__file__), "barrel.jpg")

cyl.material.texture = texture_file

scene.add_object("cylinder", cyl)
scene.run()
