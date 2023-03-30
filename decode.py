#!/usr/bin/python3
import sys
import os
import struct
from PIL import Image

if len(sys.argv) != 2:
    print("Usage: python3 decode.py [file_path]")
    sys.exit(1)

file_path = sys.argv[1]

if not os.path.isfile(file_path):
    print(f"File not found: {file_path}")
    sys.exit(1)

# Read the binary data from the file
with open(file_path, 'rb') as file:
    compressed_data = file.read()

# Save the compressed data to a file
with open('compressed.jpg', 'wb') as file:
    file.write(compressed_data)

# Decompress the data and save it to a file
with Image.open('compressed.jpg') as image:
    image.save('decoded.jpg', format='JPEG', quality=91)

