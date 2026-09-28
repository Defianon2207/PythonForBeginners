import cv2 as cv
import numpy as np

def main():
    print(f"OpenCV Version: {cv.__version__}")

    # 1. Text & Font Configuration
    text = "Hello, Mother Fathers"
    font = cv.FONT_HERSHEY_SIMPLEX
    font_scale = 0.8
    thickness = 2
    padding = 40  # Extra space around text

    # 2. Dynamically calculate exact text dimensions
    (text_width, text_height), baseline = cv.getTextSize(
        text, font, font_scale, thickness
    )

    # 3. Create canvas tailored to text size (Prevents clipping)
    canvas_width = text_width + (padding * 2)
    canvas_height = text_height + baseline + (padding * 2)
    img = np.zeros((canvas_height, canvas_width, 3), dtype=np.uint8)

    # 4. Calculate coordinates to center text perfectly
    x = (canvas_width - text_width) // 2
    y = (canvas_height + text_height - baseline) // 2

    # 5. Draw text (Yellow text for "Pila Phool" / vibrant aesthetic)
    text_color = (0, 255, 255)  # BGR format: Yellow
    cv.putText(img, text, (x, y), font, font_scale, text_color, thickness, cv.LINE_AA)

    # 6. Save image safely
    output_filename = "Mfks.png"
    if cv.imwrite(output_filename, img):
        print(f"Successfully saved to '{output_filename}' ({canvas_width}x{canvas_height}px)")

    # 7. Safe window display (Handles headless environments without crashing)
    try:
        cv.imshow("Preview", img)
        print("Press any key in the image window to exit...")
        cv.waitKey(0)
        cv.destroyAllWindows()
    except cv.error:
        print("Headless OpenCV detected (GUI display skipped).")

if __name__ == "__main__":
    main()