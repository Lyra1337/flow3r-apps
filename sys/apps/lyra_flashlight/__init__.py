from st3m.application import Application, ApplicationContext
from st3m.ui.colours import PUSH_RED, BLACK
from st3m.goose import Dict, Any
from st3m.input import InputState
from ctx import Context

import leds
import math

class Flashlight(Application):
    def __init__(self, app_ctx: ApplicationContext) -> None:
        super().__init__(app_ctx)

        for led_index in range(0, 41):
            leds.set_rgb(led_index, 0, 0, 0)

    def think(self, ins: InputState, delta_ms: int) -> None:
        leds.set_brightness(255)

        for led_index in range(9, 32):
            leds.set_rgb(led_index, 255, 255, 255)

        leds.update()

    def draw(self, ctx: Context) -> None:
        ctx.rgb(255, 255, 255).rectangle(-120, -120, 240, 240).fill()
        ctx.rgb(255, 0, 255)

        ctx.move_to(0, 0)
        ctx.save()

    def on_exit(self) -> None:
        for led_index in range(9, 32):
            leds.set_rgb(led_index, 0, 0, 0)

        leds.set_brightness(255)
        leds.update()
