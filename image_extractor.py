from PIL import Image, ImageDraw, ImageFont
import numpy as np

def create_background(width=1920, height=1080, color=(0, 0, 0)):
    """Generate a solid-color background image."""
    return Image.new("RGB", (width, height), color)

def add_text_to_image(image, text, font_path="arial.ttf", font_size=50, text_color=(255, 255, 255), position=(50, 50)):
    """Overlay text on an image."""
    draw = ImageDraw.Draw(image)
    try:
        font = ImageFont.truetype(font_path, font_size)
    except IOError:
        font = ImageFont.load_default()
    draw.text(position, text, fill=text_color, font=font)
    return image

def resize_image(image, target_width=None, target_height=None):
    """Resize image while maintaining aspect ratio."""
    if target_width and target_height:
        return image.resize((target_width, target_height))
    elif target_width:
        ratio = target_width / float(image.width)
        new_height = int(float(image.height) * ratio)
        return image.resize((target_width, new_height))
    elif target_height:
        ratio = target_height / float(image.height)
        new_width = int(float(image.width) * ratio)
        return image.resize((new_width, target_height))
    return image

# Example usage:
bg = create_background(color=(34, 34, 34))  # Dark gray
bg_with_text = add_text_to_image(bg, "PDF Summary", position=("center", "center"))
bg_with_text.save("output_bg.png")