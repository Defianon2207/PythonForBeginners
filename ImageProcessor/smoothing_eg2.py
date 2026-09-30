from pathlib import Path
import cv2 as cv

folder = Path(__file__).resolve().parent
source_path = folder / "hello.png"

image = cv.imread(str(source_path))
if image is None:
    raise FileNotFoundError(f"Could not read {source_path}")

results = {
    "average": cv.blur(image, (9, 9)),
    "gaussian": cv.GaussianBlur(image, (9, 9), 0),
    "median": cv.medianBlur(image, 9),
    "bilateral": cv.bilateralFilter(image, 9, 75, 75),
}

for name, result in results.items():
    output_path = folder / f"{name}.png"
    if not cv.imwrite(str(output_path), result):
        raise OSError(f"Could not save {output_path}")
    print("Saved:", output_path)