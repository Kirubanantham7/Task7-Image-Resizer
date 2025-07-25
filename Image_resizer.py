import os
from PIL import Image

def resize_images(input_folder, output_folder, size=(800, 600), format='JPEG'):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')):
            image_path = os.path.join(input_folder, filename)
            try:
                with Image.open(image_path) as img:
                    img = img.resize(size, Image.Resampling.LANCZOS)
                    base_name = os.path.splitext(filename)[0]
                    output_path = os.path.join(output_folder, f"{base_name}.{format.lower()}")
                    img.convert('RGB').save(output_path, format=format)
                    print(f"Resized and saved: {output_path}")
            except Exception as e:
                print(f"Failed to process {filename}: {e}")

# Paths
input_dir = r"C:\Users\Hi\Documents\python inten\Task 7\images"
output_dir = r"C:\Users\Hi\Documents\python inten\Task 7\images_resize"

# Run
resize_images(input_dir, output_dir, size=(1024, 768), format='JPEG')
