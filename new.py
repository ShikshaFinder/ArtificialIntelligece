import os

# Directory containing the fruit images
fruit_dir = 'C:\\Users\\janih\\OneDrive\\Desktop\\marketingshikshafinder\\public\\small_fruits-20240405T084032Z-001\\small_fruits'

# Get a list of all image files in the directory
fruit_images = [f for f in os.listdir(fruit_dir) if os.path.isfile(os.path.join(fruit_dir, f))]

# Print the list of image files
for image_file in fruit_images:
    print(image_file)