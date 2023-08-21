import cv2

#Configurable Parameters
source = "2.jpeg"                   #Enter the name of the image you want to resize
destination = "newImage.png"        #We can also give it png format, it will work normally with it too

percent = input("By how much percent do you want to reduce the image: ")

scale_percent = int(percent)                  # percent by which the image is resized

src = cv2.imread(source, cv2.IMREAD_UNCHANGED)
# cv2.imshow("img",image)
# cv2.waitKey(0)



# calculate the 50 percent of original dimensions
new_width = int(src.shape[1] * scale_percent / 100)  # src.shape[1] = width of the image
new_height = int(src.shape[0] * scale_percent / 100)  # src.shape[0] = height of the image

# resize image
output = cv2.resize(src, (new_width, new_height))

cv2.imwrite(destination, output)
