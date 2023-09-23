from colormath.color_objects import sRGBColor
from colormath.color_conversions import convert_color
import colormath

from lab_converter.lab2xyz.xyz import lab2xyz

def lab2rgb(l: float, a: float, b: float) -> dict:

    # convert from lab into xyz colorspace
    xyz = lab2xyz(l=l, a=a, b=b)

    # convert from xyz into rgb colorspace
    rgb = convert_color(xyz, sRGBColor)

    # extract out individual colorspace values
    r = (rgb.rgb_r / 1)*255
    g = (rgb.rgb_g / 1)*255
    b = (rgb.rgb_b / 1)*255

    # round rgb values if round parameter is true

    r_round = round(r)
    g_round = round(g)
    b_round = round(b) 

    rgb_dict = {
        'r' : r_round,
        'g' : g_round,
        'b' : b_round
    }

    return rgb_dict 


