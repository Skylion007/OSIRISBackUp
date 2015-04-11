#!/usr/bin/env python
import sys
import subprocess

# INPUT:
# Takes in the name of a video to read (videoin) and a
# resolution (res). 

# OUTPUT:
# Doesn't return a value, but decodes the input video.

def main(argv):
	videoin = str(sys.argv[1])
	res = str(sys.argv[2])

	subprocess.call("ffmpeg -i " + videoin + " -r 1 -f rawvideo - | ./lvdodec -s " + res + " -q 6 --qmin 1 --qmax 4 | mplayer -", shell=True)
	sys.exit()


if __name__ == '__main__':
	main(sys.argv[1:])