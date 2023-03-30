import sys
import os
from PIL import Image

if len(sys.argv) != 2:
    print("Usage: python3 encode.py [file_path]")
    sys.exit(1)

file_path = sys.argv[1]

if not os.path.isfile(file_path):
    print(f"File not found: {file_path}")
    sys.exit(1)

# Load the image and compress it using JPEG with quality factor 10
with Image.open(file_path) as image:
    image.save('compressed.jpg', format='JPEG', quality=10)

# Load the compressed image and convert it to binary
with open('compressed.jpg', 'rb') as file:
    compressed_data = file.read()

# Write the binary data to a file
with open('encoded.bin', 'wb') as file:
    file.write(compressed_data)
