from cmyk import CMYK
from rgb import RGB

turbo = RGB(255, 237, 0).to_cmyk()
red = RGB(255, 0, 0).to_cmyk()

mixed = turbo.mix(red)

print(mixed, mixed.to_rgb())