from st3m.application import Application, ApplicationContext
from st3m.ui.colours import PUSH_RED, BLACK
from st3m.goose import Dict, Any
from st3m.input import InputState
from ctx import Context

import leds
import math

class Blacklight(Application):
    def __init__(self, app_ctx: ApplicationContext) -> None:
        super().__init__(app_ctx)
        self.v_x = 0.0
        self.v_y = 0.0
        self.v_z = 0.0

    def think(self, ins: InputState, delta_ms: int) -> None:
        self.v_y = ins.imu.acc[0]
        self.v_x = ins.imu.acc[1]
        self.v_z = ins.imu.acc[2]

    def draw(self, ctx: Context) -> None:
        ctx.rgb(0, 0, 0).rectangle(-120, -120, 240, 240).fill()
        ctx.rgb(255, 0, 255)

        ctx.move_to(0, 0)
        ctx.save()

    def on_exit(self) -> None:
        for led_index in range(9, 33):
            leds.set_rgb(led_index, 0, 0, 0)

        leds.set_brightness(255)
        leds.update()
