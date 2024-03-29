import os
import argparse
from PIL import Image

# Create the parser
crop_parser = argparse.ArgumentParser()

# Add the arguments
crop_parser.add_argument('--img-path', type=str, required=True)
crop_parser.add_argument('--x', type=int, required=True)
crop_parser.add_argument('--y', type=int, required=True)
crop_parser.add_argument('--width', type=int, required=True)
crop_parser.add_argument('--height', type=int, required=True)
crop_parser.add_argument('--outdir', type=str, required=True)

# Parse the arguments
args = crop_parser.parse_args()

# Open the image
image = Image.open(args.img_path)

# Calculate top right corner coordinates
top_right_x = args.x + args.width
top_right_y = args.y + args.height

# Crop the image
cropped_image = image.crop((args.x, args.y, top_right_x, top_right_y))

# Create output directory if it doesn't exist
os.makedirs(args.outdir, exist_ok=True)

# Generate the output filename
base_name = os.path.basename(args.img_path)
file_name, file_extension = os.path.splitext(base_name)
counter = 1

while True:
    output_file_name = f"{file_name}_crop_{counter}{file_extension}"
    output_path = os.path.join(args.outdir, output_file_name)
    if not os.path.exists(output_path):
        break
    counter += 1

# Save the cropped image
cropped_image.save(output_path)