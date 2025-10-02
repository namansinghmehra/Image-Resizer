import os
from PIL import Image
input_folder = 'input_images'
output_folder = 'resized_images'
new_size = (800, 600)  # Set desired size (width, height)
output_format = 'PNG'  # Or use 'JPEG', 'BMP', etc.

if not os.path.exists(input_folder):
    print(f"Input folder '{input_folder}' does not exist. Please create it and add images to resize.")
    exit(1)

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        file_path = os.path.join(input_folder, filename)
        try:
            with Image.open(file_path) as img:
                img_resized = img.resize(new_size)
                base_name, _ = os.path.splitext(filename)
                output_file = f"{base_name}_resized.{output_format.lower()}"
                output_path = os.path.join(output_folder, output_file)
                img_resized.save(output_path, output_format)
                print(f"Saved {output_path}")
        except Exception as e:
            print(f"Failed to process {filename}: {e}")
