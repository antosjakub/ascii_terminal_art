import time
import os
import re

# Specify the directory
directory = 'ascii'

# List all files in the directory
file_list = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
sorted_img_list = sorted(file_list, key=lambda x: int(re.search(r'\d+', x).group()))

def print_files(files):
    for file in files:
        try:
            with open(f"{directory}/{file}", 'r') as f:
                print(f.read())
                
        except FileNotFoundError:
            print(f"Error: {file} not found.")
        
        # Wait for 0.1 seconds before moving to the next file
        time.sleep(0.035)

# Call the function with the list of files
print_files(sorted_img_list)
