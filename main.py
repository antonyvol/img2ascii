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


###	define mapping of intensivity ranges to ascii 
def grayscale_to_ascii(val):
	pass


### locally average intensivity and change it to ascii
def get_ascii_from_image(img_matrix):
	pass


def main():
	img_path = get_image_path()
	img = load_image(img_path)
	get_ascii_from_image(img)


if __name__ == "__main__":
	main()