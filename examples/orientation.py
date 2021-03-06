#!/usr/bin/python

import sys
import pyvips

a = pyvips.Image.new_from_file(sys.argv[1])

try:
    orientation = a.get('exif-ifd0-Orientation')
    a.set('orientation', int(orientation.split()[0]))
except:
    a.set('orientation', 0)

a.write_to_file(sys.argv[2])
