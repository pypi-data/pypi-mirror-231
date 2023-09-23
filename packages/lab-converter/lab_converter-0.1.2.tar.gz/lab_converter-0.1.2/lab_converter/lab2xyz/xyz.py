from colormath.color_objects import LabColor, XYZColor
from colormath.color_conversions import convert_color
import colormath

def lab2xyz(l: float, a: float, b: float) -> colormath.color_objects.XYZColor:

    # Create lab object using LabColor() function with lab values as arguments
    lab = LabColor(l,a,b)

    # convert from lab into xyz colorspace
    xyz = convert_color(lab,XYZColor)

    return xyz