import cv2
import numpy as numpy
import argparse

# Option settings
parser = argparse.ArgumentParser(description = "Process a picture.")
parser.add_argument("--folder", type=str, default="/home/tamnguyen/workplace/darknet/data/obj/", help="the picture's folder")
parser.add_argument("-p","--picture", type=str, default="3.jpg", help="picture's name")
parser.add_argument("--save", default = False, action = "store_true", help="save the picture or not")
parser.add_argument("-c","--coordinate", type=str, required=True, help="left, top, right, bot")
args = parser.parse_args()



def crop_image(left, top, right, bot):
	crop = img[top: bot, left: right]
	cv2.imshow("cropped", crop)
	# if choose to save then save the picture
	if args.save == True:
		cv2.imwrite(link, crop)

#link = "/home/tamnguyen/workplace/darknet/data/person.jpg"
coordinate = [int(item) for item in args.coordinate.split(',')]
left = coordinate[0]
top = coordinate[1]
right = coordinate[2]
bot = coordinate[3]
link = args.folder+args.picture
img = cv2.imread(link, cv2.IMREAD_COLOR)


cv2.rectangle(img, (left, top), (right, bot), (255, 0, 0), 2)
#crop_image(left, top-10, right, bot)
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
