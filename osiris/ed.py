import sys
import subprocess
from testproject.settings import BASE_DIR
import os
# INPUT:
# Takes in the name of a file to read (filein), a resolution
# (res), and the name of a file to write to (fileout). 

# OUTPUT:
# Doesn't return a value, but writes the encoded filein to
# fileout.

def encode(filein, res, fileout):
    p = os.path.join(BASE_DIR, "C/lvdoenc")
    s = "cat " + filein + " | "+ p + " -s " + res + " -q 6 --qmin 1 --qmax 4 | x264 --input-res " + res + " --fps 1 --profile high --level 5.1 --tune stillimage --crf 22 --colormatrix bt709 --me dia --merange 0 -o " + fileout + " -"
    print s
    subprocess.call(s, shell=True)


def decode(videoin, res, outputFile):
    p = os.path.join(BASE_DIR, "C/lvdodec")
    subprocess.call("ffmpeg -i " + videoin + " -r 1 -f rawvideo - | "+p +" -s " + res + " -q 6 --qmin 1 --qmax 4 | cat > "+ outputFile, shell=True)