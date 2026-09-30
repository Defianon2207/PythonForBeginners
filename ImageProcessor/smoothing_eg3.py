from pathlib import Path
import cv2 as cv

folder = Path(__file__).resolve().parent
image = cv.imread(str(folder / "hello.png"))

if image is None:
    raise FileNotFoundError("Put hello.png beside this script")

# Face rectangle: top-left corner (x, y), then width and height
x, y = 150, 80
face_width, face_height = 180, 180

# Restrict the rectangle to the image boundaries
image_height, image_width = image.shape[:2]
x1 = max(0, x)
y1 = max(0, y)
x2 = min(image_width, x + face_width)
y2 = min(image_height, y + face_height)

if x1 >= x2 or y1 >= y2:
    raise ValueError("The selected rectangle is outside the image")

face = image[y1:y2, x1:x2]
image[y1:y2, x1:x2] = cv.GaussianBlur(face, (31, 31), 0)

output = folder / "face_blurred.png"
cv.imwrite(str(output), image)
print("Saved:", output)