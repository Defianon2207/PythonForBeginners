import cv2

img = cv2.imread("Mfks.png")

center = (100, 80)
axes = (70, 40)

img = cv2.ellipse(img, center, axes, 0, 0, 360, (255, 0, 0), -1)

cv2.imshow("Ellipse 1", img)
cv2.waitKey(0)
cv2.destroyAllWindows()