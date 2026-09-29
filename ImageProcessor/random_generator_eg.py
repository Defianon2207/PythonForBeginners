import cv2 as cv
import numpy as np

width, height = 800, 500

# Each pixel gets random Blue, Green, and Red values from 0 to 255.
rng = np.random.default_rng()
image = rng.integers(
    0, 256,
    size=(height, width, 3),
    dtype=np.uint8,
)

cv.imwrite("random_image.png", image)
print("Saved random_image.png")