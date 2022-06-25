
#June 6, 2022 Ann Franks murder was 78 years ago https://www.youtube.com/watch?v=vBKK3yxk5jY&feature=youtu.be
import time
import board
import neopixel
import digitalio
print("Hello World!!")
#Config Neopixel String
class Fast_PX_Config():
    def __init__(self, preConfig=True, autoWrite=True):
        self.defaultBrightness = 0.1
        self.preConfig = preConfig
        if(self.preConfig):
            #Config all pins as Neopixel
            self.Strings = {
                0: {
                    "pin": board.D0, "n": 60, "bpp": 4, 
                    "auto_write": autoWrite, "pixel_order": neopixel.GRBW,
                    "brightness": self.defaultBrightness
                },
                1: {
                    "pin": board.D1, "n": 60, "bpp": 4, 
                    "auto_write": autoWrite, "pixel_order": neopixel.GRBW,
                    "brightness": self.defaultBrightness
                },
                2: {
                    "pin": board.D2, "n": 60, "bpp": 4, 
                    "auto_write": autoWrite, "pixel_order": neopixel.GRBW,
                    "brightness": self.defaultBrightness
                },
                3: {
                    "pin": board.D3, "n": 60, "bpp": 4, 
                    "auto_write": autoWrite, "pixel_order": neopixel.GRBW,
                    "brightness": self.defaultBrightness
                },
                4: {
                    "pin": board.D4, "n": 60, "bpp": 4, 
                    "auto_write": autoWrite, "pixel_order": neopixel.GRBW,
                    "brightness": self.defaultBrightness}
                # },
                # 5: {
                #     "pin": board.D5, "n": 60, "bpp": 4, 
                #     "auto_write": autoWrite, "pixel_order": neopixel.GRBW,
                #     "brightness": self.defaultBrightness
                # },
                # 6: {
                #     "pin": board.D6, "n": 60, "bpp": 4, 
                #     "auto_write": autoWrite, "pixel_order": neopixel.GRBW,
                #     "brightness": self.defaultBrightness
                # },
                # 7: {
                #     "pin": board.D7, "n": 60, "bpp": 4, 
                #     "auto_write": autoWrite, "pixel_order": neopixel.GRBW,
                #     "brightness": self.defaultBrightness
                # },
                # 8: {
                #     "pin": board.D8, "n": 60, "bpp": 4, 
                #     "auto_write": autoWrite, "pixel_order": neopixel.GRBW,
                #     "brightness": self.defaultBrightness
                # }
            }
cfg = Fast_PX_Config(preConfig=True,autoWrite=False)
pxls = []
for index, s in cfg.Strings.items():
    pxls.append(neopixel.NeoPixel(
        s["pin"], s["n"], bpp = s["bpp"], 
        brightness = s["brightness"], 
        auto_write = s["auto_write"], 
        pixel_order = s["pixel_order"]
        ) 
    )

Colors = [(255,255,255,255), (255,0,0,0),(0,255,0,0),(0,0,255,0),(0,0,0,255)]

#Confit Boot Button
#button = digitalio.DigitalInOut(board.BUTTON)
i = 0
while True:
    for p in pxls:
        p.fill(Colors[i])
        p.show()
    time.sleep(1)
    i+=1
    if i > len(Colors) -1:
        i = 0