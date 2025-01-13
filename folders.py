import os
import json

# Path to the gallery directory
gallery_dir = 'gallery'

# Get all directories in the gallery directory
folders = [f for f in os.listdir(gallery_dir) if os.path.isdir(os.path.join(gallery_dir, f))]

# Sort the folders by name (in descending order)
folders.sort(reverse=True)

last_five_folders = folders[:]

# Write the result to folders.json
with open('folders.json', 'w', encoding='utf-8') as json_file:
    json.dump(last_five_folders, json_file, ensure_ascii=False, indent=2)

print('folders.json has been generated successfully!')
