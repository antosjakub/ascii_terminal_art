import os
import re
from PIL import Image
import sys

# ASCII characters used for intensity levels, from darkest to lightest
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

# Function to resize the image
def resize_image(image, new_width=100):
    width, height = image.size
    aspect_ratio = height / width / 1.65  # Adjust aspect ratio for text (optional)
    new_height = int(new_width * aspect_ratio)
    return image.resize((new_width, new_height))

# Function to convert image to grayscale
def grayify(image):
    return image.convert("L")

# Function to map each pixel to an ASCII character
def pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = "".join([ASCII_CHARS[pixel // 25] for pixel in pixels])
    return ascii_str

# Main function to convert an image file to ASCII text
def image_to_ascii(image_path, output_path="output.txt", new_width=100):
    try:
        # Load the image
        image = Image.open(image_path)
    except Exception as e:
        print(e)
        return

    # Convert and resize image
    image = resize_image(image, new_width)
    image = grayify(image)

    # Convert pixels to ASCII characters
    ascii_str = pixels_to_ascii(image)

    # Format ASCII string to match the image dimensions
    pixel_count = len(ascii_str)
    ascii_img = "\n".join([ascii_str[i:(i + new_width)] for i in range(0, pixel_count, new_width)])

    # Save to file
    with open(output_path, "w") as f:
        f.write(ascii_img)

    print(f"ASCII art saved to {output_path}")

# Specify the directories
dir_imgs = sys.argv[1]  # dir with .pngs source files
dir_ascii = sys.argv[2] # where to store ascii .txt files
os.makedirs(dir_ascii, exist_ok=True)

# List all files in the directory
files = [f for f in os.listdir(dir_imgs) if os.path.isfile(os.path.join(dir_imgs, f))]
sorted_files = sorted(files, key=lambda x: int(re.search(r'\d+', x).group()))

# Save to ASCII
i = 1
for file in sorted_files:
    image_to_ascii(f"{dir_imgs}/{file}", output_path=f"{dir_ascii}/frame_{i}.txt", new_width=120)
    print(i, file)
    i += 1