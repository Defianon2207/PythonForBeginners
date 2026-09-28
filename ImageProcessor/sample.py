import cv2
import numpy as np


def overlay_rgba(background, overlay, x, y):
    overlay_height, overlay_width = overlay.shape[:2]
    background_height, background_width = background.shape[:2]

    # Keep the overlay within the frame.
    if x < 0 or y < 0:
        return background

    if (
        x + overlay_width > background_width
        or y + overlay_height > background_height
    ):
        return background

    rgb = overlay[:, :, :3].astype(float)
    alpha = overlay[:, :, 3].astype(float) / 255.0
    alpha = alpha[:, :, np.newaxis]

    region = background[
        y:y + overlay_height,
        x:x + overlay_width,
    ].astype(float)

    blended = alpha * rgb + (1 - alpha) * region

    background[
        y:y + overlay_height,
        x:x + overlay_width,
    ] = blended.astype(np.uint8)

    return background


video = cv2.VideoCapture("input.mp4")
overlay_image = cv2.imread(
    "glasses.png",
    cv2.IMREAD_UNCHANGED,
)

fps = video.get(cv2.CAP_PROP_FPS)
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

writer = cv2.VideoWriter(
    "output.mp4",
    cv2.VideoWriter_fourcc(*"mp4v"),
    fps,
    (width, height),
)

while True:
    success, frame = video.read()

    if not success:
        break

    # These would normally come from MediaPipe landmarks.
    left_eye = (250, 180)
    right_eye = (390, 185)

    eye_distance = int(
        np.linalg.norm(
            np.array(right_eye) - np.array(left_eye)
        )
    )

    overlay_width = int(eye_distance * 1.7)

    aspect_ratio = (
        overlay_image.shape[0]
        / overlay_image.shape[1]
    )

    overlay_height = int(overlay_width * aspect_ratio)

    resized_overlay = cv2.resize(
        overlay_image,
        (overlay_width, overlay_height),
    )

    center_x = (left_eye[0] + right_eye[0]) // 2
    center_y = (left_eye[1] + right_eye[1]) // 2

    x = center_x - overlay_width // 2
    y = center_y - overlay_height // 2

    frame = overlay_rgba(
        frame,
        resized_overlay,
        x,
        y,
    )

    writer.write(frame)

video.release()
writer.release()