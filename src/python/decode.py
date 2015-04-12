#!/usr/bin/env python
import sys
import subprocess

# INPUT:
# Takes in the name of a video to read (videoin), a
# resolution (res), and the name of a video to write
# to (videoout).

# OUTPUT:
# Doesn't return a value, but decodes the input video.

def main(argv):
	videoin = str(sys.argv[1])
	res = str(sys.argv[2])
	videoout = str(sys.argv[3])

	subprocess.call("unzip " + videoin + " | ffmpeg -i - -r 1 -f rawvideo - | ../C/./lvdodec -s " + res + " -q 6 --qmin 1 --qmax 4 | cat > " + videoout, shell=True)
	sys.exit()


if __name__ == '__main__':
	main(sys.argv[1:])