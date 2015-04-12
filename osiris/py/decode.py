#!/usr/bin/env python
import sys
import subprocess

# INPUT:
# Takes in the name of a video to read (videoin) and a
# resolution (res). 

# OUTPUT:
# Doesn't return a value, but decodes the input video.

def decode(videoin, res):

	subprocess.call("ffmpeg -i " + videoin + " -r 1 -f rawvideo - | ../C/./lvdodec -s " + res + " -q 6 --qmin 1 --qmax 4 | mplayer -", shell=True)
	sys.exit()

