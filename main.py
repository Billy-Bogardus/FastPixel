
#June 6, 2022 Ann Franks murder was 78 years ago https://www.youtube.com/watch?v=vBKK3yxk5jY&feature=youtu.be
import time
import board
import neopixel
import digitalio

from rainbowio import colorwheel

print("Hello World!!")
#Config Neopixel String
class Fast_PX_Config():
    """
    A Class defining Fast Pixel Strngs and how to configure them
    param: preConfig defaults to true. If true Default settings are applied
    param: autoWrite defaults to true. If true pixel.show() does not need to be called
    param: defalute Brightness sets brightness from 0.0 to 0.1
    """
    def __init__(self, 
        preConfig: bool =True, 
        autoWrite: bool =True,
        defaultBrightness: float = 0.1
        ):
        self.defaultBrightness = defaultBrightness
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
# Rainbow
num_pixels = 60
wait = 0.0
Colors = [ [] for x in range(num_pixels)] 
for j in range(255):
    for i in range(num_pixels):
        #print("i")
        rc_index = (i * 256 // num_pixels) + j
        Colors[i] = colorwheel(rc_index & 255)
if True:
    print(type(pxls))
    #print("ping")
b = 0.1
a = 1
while True:
    if a:
        b+=0.01
    else:
        b-=0.01
    for p in pxls:
        p[0:num_pixels] = Colors
        p.brightness = b
        p.show()
    if b >= 1.0:
        a = 0
    if b <= 0.1:
        a = 1
    Colors = Colors[1:] + Colors[:1]
    time.sleep(wait)
     
# # # Alternating Colors
while True:
    for p in pxls:
        p.fill(Colors[i])
        p.show()
    #time.sleep(1)
    i+=1
    if i > len(Colors) -1:
        i = 0