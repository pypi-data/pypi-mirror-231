from .rgb import lab2rgb
from .lab2xyz.rgb_value_checker import rgb_value_checker
from .lab2xyz.read_conversion_csv import extract_store_base10_hex_conversion


def lab2hex(l: float, a: float, b: float, hex_conversion_csv_path: str) -> dict:
    rgb_dict = lab2rgb(l=l, a=a, b=b)
    rgb_dict_checked = rgb_value_checker(rgb_dict=rgb_dict)

    r = rgb_dict_checked['r']
    g = rgb_dict_checked['g']
    b = rgb_dict_checked['b']

    hex_pos1 = ''
    hex_pos2 = ''
    hex_pos3 = ''

    hex_conversion_csv = extract_store_base10_hex_conversion(hex_conversion_csv_path)

    for i, row in hex_conversion_csv.iterrows():
        if r == row['base10']:
            hex_pos1 = row['hex']
        if g == row['base10']:
            hex_pos2 = row['hex']
        if b == row['base10']:
            hex_pos3 = row['hex']
    hex_color_value = f"#{hex_pos1}{hex_pos2}{hex_pos3}" 

    return hex_color_value





