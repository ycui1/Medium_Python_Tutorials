# %%
import cv2

original = cv2.imread('original.jpg')
print("Data Type:", type(original))
print("Image Shape:", original.shape)
print("Image Size:", original.size)
print("Element Type:", original.dtype)
print("Value Range:", original.min(), '-', original.max())

# Resize Images
for width in (100, 200, 400):
    resized = cv2.resize(original, (width, width), interpolation=cv2.INTER_LINEAR)
    print("Resized Image Width:", resized.shape[0])
    cv2.imwrite(f"resized_{width}.jpg", resized)

# Color to Grayscale
gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
print("Gray Scale Image Shape:", gray.shape)
print("Gray Scale Image Size", gray.size)
cv2.imwrite("original_gray.jpg", gray)

# Create images of solid colors
# import numpy for image manipulation purposes
import numpy as np


def image_with_color(color, size):
    color_image = np.ones(shape=[size[1], size[0], 3], dtype=np.uint8)
    for color_index, color_value in enumerate(color):
        color_image[:, :, color_index] = color_value
    return color_image


bgr = {'blue': (255, 0, 0), 'green': (0, 255, 0), 'red': (0, 0, 255)}
target_size = (500, 500)
solid_colors = dict()

for color_name, color in bgr.items():
    print("Creating an image with color:", color_name)
    color_image = image_with_color(color, target_size)
    solid_colors[color_name] = color_image


# Use dictionary comprehension
# solid_colors = {color_name: image_with_color(color, target_size) for color_name, color in bgr.items()}


# Overlay images
def overlay(front_image, back_image, position=(0, 0)):
    x_offset, y_offset = position
    back_image[y_offset:y_offset + front_image.shape[0], x_offset:x_offset + front_image.shape[1]] = front_image
    return back_image


for width, (color_name, color_image) in zip((100, 200, 400), solid_colors.items()):
    resized_image = cv2.imread(f"resized_{width}.jpg")
    overlaid = overlay(resized_image, color_image)
    cv2.imwrite(f"overlaid_{color_name}.jpg", overlaid)


# Add text
image_blue = cv2.imread("overlaid_blue.jpg")
image_text = cv2.putText(image_blue,
                         "Hi, Python Learners!",
                         (0, 250),
                         cv2.FONT_HERSHEY_DUPLEX,
                         1,
                         (255, 255, 255))
cv2.imwrite("image_text.jpg", image_text)


# A generic function to draw text, at center by default
def draw_text(image, text, font_scale, color, x=None, y=None):
    font = cv2.FONT_HERSHEY_DUPLEX
    thickness = 1
    image_height, image_width = image.shape[0], image.shape[1]
    text_width, text_height = cv2.getTextSize(text, font, font_scale, thickness)[0]
    if x is None:
        x = (image_width - text_width) // 2
    if y is None:
        y = (image_height + text_height) // 2
    cv2.putText(image, text, (x, y), font, font_scale, color, thickness, cv2.LINE_AA)
    return image

image_blue = cv2.imread("overlaid_blue.jpg")
image_text_center = draw_text(image_blue, "Hi, Python Learners!", 1, (255, 255, 255))
cv2.imwrite("image_text_center.jpg", image_text_center)

# Rotate the images
overlaid_blue = cv2.imread('overlaid_blue.jpg')
rotations = {90: cv2.ROTATE_90_CLOCKWISE, 180: cv2.ROTATE_180, 270: cv2.ROTATE_90_COUNTERCLOCKWISE}
for angle, rotation in rotations.items():
    rotated = cv2.rotate(overlaid_blue, rotation)
    rotated = draw_text(rotated, f"Rotate {angle} degrees", 1, (255, 255, 255))
    cv2.imwrite(f"image_rotated_{angle}.jpg", rotated)


# Flip the images
rotated = cv2.imread('image_rotated_90.jpg')
flips = {'h': 1, 'v': 0, 'h-v': -1}
for flip_name, flip_code in flips.items():
    flipped = cv2.flip(rotated, flip_code)
    flipped = draw_text(flipped, flip_name, 1, (255, 255, 255), y=400)
    cv2.imwrite(f"image_flipped_{flip_name}.jpg", flipped)