from st3m.application import Application, ApplicationContext
from st3m.ui.colours import PUSH_RED, BLACK
from st3m.goose import Dict, Any
from st3m.input import InputState
from ctx import Context
import leds

import json
import math


class Configuration:
    def __init__(self) -> None:
        self.name = "Lyra"
        self.alt_name = "Tom"
        self.size: int = 110
        self.font: int = 6

    @classmethod
    def load(cls) -> "Configuration":
        res = cls()
        return res

class NickApp(Application):
    def __init__(self, app_ctx: ApplicationContext) -> None:
        super().__init__(app_ctx)
        self._scale = 1.0
        self._led = 0.0
        self._phase = 0.0
        self._config = Configuration.load()
        leds.set_brightness(255)

    def draw(self, ctx: Context) -> None:
        ctx.text_align = ctx.CENTER
        ctx.text_baseline = ctx.MIDDLE
        ctx.font_size = self._config.size
        ctx.font = ctx.get_font_name(self._config.font)

        ctx.rgb(0, 0, 0).rectangle(-120, -120, 240, 240).fill()
        ctx.rgb(255, 0, 255)

        ctx.move_to(0, 0)
        ctx.save()
        ctx.scale(abs(self._scale), 1)
        
        if self._scale < 0:
            ctx.text(self._config.name)
        else:
            ctx.text(self._config.alt_name)

        ctx.restore()

        leds.set_hsv(int(self._led), abs(self._scale) * 360, 1, 0.2)
        leds.set_rgb(int((self._led + 32) % 40), 0, 0, 0)

        leds.update()
        # ctx.fill()

    # def on_exit(self) -> None:
    #     self._config.save(self._filename)

    def think(self, ins: InputState, delta_ms: int) -> None:
        super().think(ins, delta_ms)

        self._phase += delta_ms / 500
        self._scale = math.sin(self._phase)
        self._led += delta_ms / 45
        if self._led >= 40:
            self._led = 0
