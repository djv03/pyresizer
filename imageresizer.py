import cv2
import easygui
# print(easygui.fileopenbox())

source = easygui.fileopenbox()
destination = "dhruvin_resized2.jpg"
scale_percent = 60

src=cv2.imread(source, cv2.IMREAD_UNCHANGED)

# defining heigh and width of the image
new_height = int(src.shape[0] * scale_percent / 100)
new_width = int(src.shape[1] * scale_percent / 100)

#resizing the image
output = cv2.resize(src, (new_width, new_height))

# Compress the image using JPEG format and save it
cv2.imwrite(destination, output)
