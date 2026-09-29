import cv2 as cv
import numpy as np

width, height = 800, 500
image = np.zeros((height, width, 3), dtype=np.uint8)  # Black image
rng = np.random.default_rng(seed=42)  # Same random drawing each run

def random_point():
    x = int(rng.integers(0, width))
    y = int(rng.integers(0, height))
    return (x, y)

def random_color():
    # OpenCV uses Blue, Green, Red order
    return tuple(int(value) for value in rng.integers(0, 256, size=3))

# Draw 30 random lines
for _ in range(30):
    cv.line(
        image,
        random_point(),
        random_point(),
        random_color(),
        thickness=int(rng.integers(1, 6)),
    )

# Draw 15 random circles
for _ in range(15):
    cv.circle(
        image,
        center=random_point(),
        radius=int(rng.integers(10, 70)),
        color=random_color(),
        thickness=2,
    )

# Draw text at a random position
cv.putText(
    image,
    "Hello OpenCV!",
    random_point(),
    cv.FONT_HERSHEY_SIMPLEX,
    1.0,                  # Font scale
    random_color(),
    2,                    # Thickness
    cv.LINE_AA,
)

cv.imwrite("random_drawing.png", image)
print("Saved random_drawing.png")