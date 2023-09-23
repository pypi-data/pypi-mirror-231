## LAB Converter Python Package

### Prerequisites
#### ___Hex Conversion .csv___
In order to convert lab values to a hex code for a given color, down load [this csv](https://drive.google.com/file/d/1PflPAkflHUm5UClnMx_HRDw14ry535QZ/view?usp=sharing) containing hex codes mapped to the corresponding rbg value.

### Installation
```
pip install lab_converter
```

### Usage
```
from lab_converter import lab2hex

hex = lab2hex(52.9, 8.88, 54.53, hex_conversion_csv_path="./Base10_Hex.csv")

print(hex)
```


