
#June 6, 2022 Ann Franks murder was 78 years ago https://www.youtube.com/watch?v=vBKK3yxk5jY&feature=youtu.be
import time
import board
import neopixel
import digitalio

#Config Neopixel String
pixel1 = neopixel.NeoPixel(board.D1, 60,pixel_order=neopixel.RGBW)
pixel2 = neopixel.NeoPixel(board.D2, 60,pixel_order=neopixel.RGBW)
pixel3 = neopixel.NeoPixel(board.D3, 60,pixel_order=neopixel.RGBW)
pixel4 = neopixel.NeoPixel(board.D4, 60,pixel_order=neopixel.RGBW)
pixel5 = neopixel.NeoPixel(board.D0, 60,pixel_order=neopixel.RGBW)
pixel1.brightness = 0.1# 0.3
pixel2.brightness = 0.1# 0.3
pixel3.brightness = 0.1# 0.3
pixel4.brightness = 0.1# 0.3
pixel5.brightness = 0.1# 0.3

#Confit Boot Button
#button = digitalio.DigitalInOut(board.BUTTON)

while True:
    pixel1.fill((255, 255, 255, 255))
    pixel2.fill((255, 255, 255, 255))
    pixel3.fill((255, 255, 255, 255))
    pixel4.fill((255, 255, 255, 255))
    pixel5.fill((255, 255, 255, 255))
    time.sleep(1)
    pixel1.fill((255, 0, 0,0))
    pixel2.fill((255, 0, 0,0))
    pixel3.fill((255, 0, 0,0))
    pixel4.fill((255, 0, 0,0))
    pixel5.fill((255, 0, 0,0))
    time.sleep(1)
    pixel1.fill((0, 255, 0,0))
    pixel2.fill((0, 255, 0,0))
    pixel3.fill((0, 255, 0,0))
    pixel4.fill((0, 255, 0,0))
    pixel5.fill((0, 255, 0,0))
    time.sleep(1)
    pixel1.fill((0, 0, 255, 0))
    pixel2.fill((0, 0, 255, 0))
    pixel3.fill((0, 0, 255, 0))
    pixel4.fill((0, 0, 255, 0))
    pixel5.fill((0, 0, 255, 0))
    time.sleep(1)
    pixel1.fill((0, 0, 0, 255))
    pixel2.fill((0, 0, 0, 255))
    pixel3.fill((0, 0, 0, 255))
    pixel4.fill((0, 0, 0, 255))
    pixel5.fill((0, 0, 0, 255))
    time.sleep(1)
