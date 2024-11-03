from main import *
import os

# Specify the directory
directory = '5k'
output_dir = 'ascii_2'


# List all files in the directory
files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]


i = 1
for file in files:
    image_to_ascii(f"{directory}/{file}", output_path=f"{output_dir}/rick_frame_{i}.txt", new_width=120)
    i += 1