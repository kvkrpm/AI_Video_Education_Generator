import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

def create_slide(text, image_path=None, size=(1280, 720)):
    img = Image.new('RGB', size, color=(255, 255, 255))
    draw = ImageDraw.Draw(img)

    font = ImageFont.truetype("arial.ttf", 40)  # You can change font
    margin = 40
    offset = 100

    # Wrap text
    for line in textwrap.wrap(text, width=40):
        draw.text((margin, offset), line, font=font, fill="black")
        offset += 60

    # If image exists, paste it
    if image_path:
        with Image.open(image_path).convert("RGB") as img2:
            img2 = img2.resize((640, 360))
            img.paste(img2, (320, 300))

    return cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

def generate_video(slides, output_path="generated_video.avi", fps=1):
    size = (1280, 720)
    out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'XVID'), fps, size)

    for slide in slides:
        out.write(slide)

    out.release()
    print(f"Video saved to {output_path}")

