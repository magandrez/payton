import sdl2

from payton.scene import Scene
from payton.scene.controller import Controller


class CustomKeyboardControls(Controller):
    def keyboard(self, event, scene):
        # Do we want all other keyboard maps? if so, lets super this!
        super().keyboard(event, scene)
        if event.type == sdl2.SDL_KEYUP:
            key = event.key.keysym.sym
            if key == sdl2.SDLK_s:
                print("Key S is pressed!")


scene = Scene()
scene.controller = CustomKeyboardControls()

scene.run()
