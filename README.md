 Task7-Image-Resizer
 ---------------------

 Image Resizer Tool
A Python-based batch image resizer that automates the task of resizing and converting multiple images from a folder using the Pillow library.

✅ Features
-------------------

Batch resize all images in a folder

Convert images to desired format (JPEG, PNG, etc.)

Automatically saves resized images in a new folder

Lightweight and easy to modify

📁 Project Structure
-------------------------
Task 7/
│
├── images/               # Original input images
├── images_resize/        # Output resized images
├── resize_script.py      # Python script
└── README.md             # This file

🛠️ Requirements
-------------------
Python 3.x

Pillow (pip install pillow)

🚀 How to Use
---------------
Install dependencies


pip install pillow
Update the script with your desired folder paths and image size:

python

input_dir = r"C:\Users\Hi\Documents\python inten\Task 7\images"
output_dir = r"C:\Users\Hi\Documents\python inten\Task 7\images_resize"
resize_images(input_dir, output_dir, size=(1024, 768), format='JPEG')
Run the script


python resize_script.py
Check the output folder for resized images.

🧪 Sample Output
-----------------------
Original Image	Resized Image

📸  screenshots 
-----------------
before - image
--------------
![before resize Screenshot](images/c1.png)

after - image
-------------
![after resize Screenshot](images/c3.png).


🧾 Notes
------------

Supports .jpg, .jpeg, .png, .gif, .bmp, .tiff

Images are resized using LANCZOS filter for high-quality output

Converts all images to the specified format (e.g., JPEG)
