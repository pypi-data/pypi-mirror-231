def rgb_value_checker(rgb_dict: dict) -> dict:
    if rgb_dict['r'] > 255:
        rgb_dict['r'] = 255
    
    if rgb_dict['g'] > 255:
        rgb_dict['g'] = 255

    if rgb_dict['b'] > 255:
        rgb_dict['b'] = 255
    
    return rgb_dict