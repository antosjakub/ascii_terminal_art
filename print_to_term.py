import time
import os
import re
import sys
import pygame


directory = sys.argv[1]
dir_ascii = f"{directory}/ascii"
dir_sound = f"{directory}/sound.mp3"

PLAY_SOUND = False
if os.path.exists(dir_sound):
    PLAY_SOUND = True

    # Initialize the pygame mixer
    pygame.mixer.init()
    # Load your MP3 file
    pygame.mixer.music.load(dir_sound)
    # Play the sound
    pygame.mixer.music.play()


# directory containing the ascii txt files:

# List all files in the directory
file_list = [f for f in os.listdir(dir_ascii) if os.path.isfile(os.path.join(dir_ascii, f))]
sorted_img_list = sorted(file_list, key=lambda x: int(re.search(r'\d+', x).group()))

def print_files(files):
    for file in files:
        try:
            with open(f"{dir_ascii}/{file}", 'r') as f:
                print(f.read())
                
        except FileNotFoundError:
            print(f"Error: {file} not found.")
        
        # Wait for 0.1 seconds before moving to the next file
        time.sleep(0.035)

# Call the function with the list of files
print_files(sorted_img_list)


if PLAY_SOUND:
    # Wait until the sound finishes playing
    while pygame.mixer.music.get_busy():  # Check if music is still playing
        pygame.time.Clock().tick(10)  # Wait 10 ms to avoid high CPU usage
