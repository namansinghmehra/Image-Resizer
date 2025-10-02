# Image Resizer

A simple Python script to resize images in bulk.

## Description

This script takes images from the `input_images` folder, resizes them to a specified size (800x600 by default), and saves the resized images in the `resized_images` folder.

## Requirements

- Python 3.x
- Pillow (PIL) library

Install Pillow using pip:
```
pip install pillow
```

## Usage

1. Create a folder named `input_images` in the same directory as the script.
2. Place the images you want to resize in the `input_images` folder. Supported formats: PNG, JPG, JPEG, BMP, GIF.
3. Run the script:
   ```
   python image_resizer.py
   ```
4. The resized images will be saved in the `resized_images` folder with "_resized" appended to the filename.

## Configuration

You can modify the following variables in the script:
- `input_folder`: Path to the input folder (default: 'input_images')
- `output_folder`: Path to the output folder (default: 'resized_images')
- `new_size`: Tuple for the new size (width, height) (default: (800, 600))
- `output_format`: Output format (default: 'PNG')

## Notes

- The script will create the output folder if it doesn't exist.
- If the input folder doesn't exist, the script will exit with an error message.
- Original images are not modified.
