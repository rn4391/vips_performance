import sys
import shutil
import time
import copy
from os import listdir, remove, path, system
from os.path import isfile, join

import gi
gi.require_version('Vips', '8.0')
from gi.repository import Vips

print "clearing output directory - " + sys.argv[2]
for f in listdir(sys.argv[2]):
    remove(join(sys.argv[2], f))

fileName = ""
targetHeight = [1000.0, 750.0, 500.0, 250.0, 100.0, 1500.0, 1000.0, 750.0, 500.0, 250.0, 100.0, 1500.0, 1000.0, 750.0, 500.0, 250.0, 100.0, 1500.0]
imageScale = 0.0

for f in listdir(sys.argv[1]):
    if isfile(join(sys.argv[1], f)):
        i = Vips.Image.new_from_file(join(sys.argv[1], f))
        
        for h in targetHeight:
            im = i;
            imageScale = h/im.height
            im = im.similarity(scale = imageScale)
            im = im.affine([0, -1, 1, 0])
            # The height and width obtained after the previous two operations
            # and not of the original one
            # print(im.height)
            # print(im.width);
            im = im.extract_area(10, 10, im.width - 20, im.height - 20)
            im.write_to_file(join(sys.argv[2], str(int(h)) +"_"+str(f)))