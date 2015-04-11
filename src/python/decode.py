
import sys
import subprocess

# INPUT:
# Takes in the name of a video to read (videoin) and a resolution
# (res).

# OUTPUT:
# Doesn't return a value, but writes the encoded filein to
# fileout.

def main(argv):

	videoin = str(sys.argv[1])
	res = str(sys.argv[2])
	fileout = str(sys.argv[3])

	subprocess.call("cat filein | ../C/./lvdoenc -s res -q 6 --qmin 1 --qmax 4 | x264 --input-res res --fps 1 --profile high --level 5.1 --tune stillimage --crf 22 --colormatrix bt709 --me dia --merange 0 -o fileout -", shell=True)

	sys.exit()


if __name__ == '__main__':
	main(sys.argv[1:])