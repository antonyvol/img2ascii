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
	pass


### locally average intensivity and change it to ascii
def get_ascii_from_image(img_matrix):
	conv_ratio = 5
	conv_img = np.empty(shape=[int(np.size(img_matrix,0)/conv_ratio), int(np.size(img_matrix,1)/conv_ratio)], dtype=int)
	
	oi = 0 # original i
	oj = 0 # original j
	ci = 0 # convoluted i
	cj = 0 # convoluted j
	while oi < np.size(img_matrix,0): # convolve image
		oj = 0
		cj = 0
		while oj < np.size(img_matrix,0):
			res = 0

			pass # for oi, oi + cr, oj, oj + cr convolute to conv_img[ci, cj]

			oj = oj + conv_ratio
			cj = cj + 1
		oi = oi + conv_ratio
		ci = ci + 1





def main():
	img_path = get_image_path()
	img = load_image(img_path)
	get_ascii_from_image(img)


if __name__ == "__main__":
	main()