import os
from dictionaries import Animals, Apparel
names = Animals.all_names
formats_blank = Apparel.blank_image_name_formats
formats_red = Apparel.red_image_name_formats

for name in names:
    print name

for format in formats_red:
    print format

for format in formats_blank:
    print format
