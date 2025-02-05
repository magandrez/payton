import os
import math
from payton.scene import Scene
from payton.scene.geometry import Sphere
from payton.scene.light import Light


def motion(name, scene, period, total):
    angle = (total * 10) % 360
    px = math.cos(math.radians(angle)) * 8
    py = math.sin(math.radians(angle)) * 8
    scene.objects["nucleus"].children["particle"].position = [px, py, 0]

    sx = math.cos(math.radians(angle * 10)) * 2  # 10 times faster
    sy = math.sin(math.radians(angle * 10)) * 2
    scene.objects["nucleus"].children["particle"].children[
        "sub_particle"
    ].position = [sx, sy, 0]
    scene.lights[0].position = [px, py, 0]
    scene.lights[1].position = [-px, -py, 0]


space = Scene()
space.lights.append(Light())
space.observers[0].position = [20, 20, 20]
space.grid.resize(40, 40, 1)

texture_file = os.path.join(os.path.dirname(__file__), "map.png")

nucleus = Sphere(radius=5, parallels=36, meridians=36)
nucleus.material.texture = texture_file
particle = Sphere()
particle.position = [8, 0, 0]

sub_particle = Sphere(radius=0.5)
sub_particle.position = [0, 2, 0]

nucleus.add_child("particle", particle)
particle.add_child("sub_particle", sub_particle)

space.add_object("nucleus", nucleus)

space.create_clock("motion", 0.01, motion)
print("Hit SPACE to continue animation")
space.run()
