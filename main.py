import argparse
from PIL import Image
import numpy as np


### retrieving image path from command line argument
def get_image_path():
	print("Running script: " + __name__)
	parser = argparse.ArgumentParser()
	parser.add_argument("img_path")
	args = parser.parse_args()
	print("Path to image: " + args.img_path)
	return args.img_path


### loading the image and making it grayscale
def load_image(img_path):
	img = Image.open(img_path)
	img = img.convert('L') # grayscale
	img_matrix = np.asarray(img.getdata()).reshape(img.size[0], img.size[1]) # intensivity matrix
	print("Converted to grayscale")
	return img_matrix


### define mapping of intensivity ranges to ascii 
def grayscale_to_ascii(val):
	# using 9-level system from this article
	# https://www.codeproject.com/Articles/20435/Using-C-To-Generate-ASCII-Art-From-An-Image
	if val > 230:
		return " "
	elif val > 200:
		return "."
	elif val > 180:
		return "*"
	elif val > 160:
		return ":"
	elif val > 130:
		return "o"
	elif val > 100:
		return "&"
	elif val > 70:
		return "8"
	elif val > 50:
		return "#"
	else:
		return "@"


### locally average intensivity and change it to ascii
def get_ascii_from_image(img_matrix):
	conv_ratio = 5

	print("--------------------DEBUG DATA----------------------------")
	print("img_matrix: (" + str(np.size(img_matrix, 0)) + "," + str(np.size(img_matrix, 1)) + ")")

	ascii_img = []

	for i in range(0, np.size(img_matrix, 0), conv_ratio):
		ascii_line = []
		for j in range(0, np.size(img_matrix, 1), conv_ratio):
			# check if current window is not OOB for img_matrix
			if i + conv_ratio >= np.size(img_matrix, 0) or j + conv_ratio >= np.size(img_matrix, 1):
				continue
			res = 0
			for ti in range(i, i + conv_ratio):
				for tj in range(j, j + conv_ratio):
					res = res + img_matrix[ti][tj] # sum intensivities in current window
			ascii_line.append(grayscale_to_ascii(int(res/(conv_ratio ** 2)))) # get avg intensivity and make it ascii
		if ascii_line: # check in case of early stop for OOB prevention
			ascii_img.append(ascii_line)

	print("ascii_img: (" + str(len(ascii_img)) + "," + str(len(ascii_img[0])) + ")")

	return ascii_img


def main():
	img_path = get_image_path()
	img = load_image(img_path)
	ascii_img = get_ascii_from_image(img)

	f = open("out.txt", "w")
	for i in range(len(ascii_img)):
		for j in range(len(ascii_img[0])):
			f.write(ascii_img[i][j])
		f.write("\n")
	f.close()

if __name__ == "__main__":
	main()