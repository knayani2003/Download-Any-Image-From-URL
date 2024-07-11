# Download-Any-Image-From-URL
import requests
import os

# URLs of the images you want to download
image_urls = [
 "https://rukminim2.flixcart.com/image/832/832/xif0q/backpack/n/j/n/9-diva-19-girls-13-bkpdivagl1903-backpack-gear-41-19-original-imahybt25yzrfhcu.jpeg?q=70&crop=false",
 "https://rukminim2.flixcart.com/image/832/832/xif0q/backpack/7/n/0/9-diva-19-girls-13-bkpdivagl1903-backpack-gear-41-19-original-imahybt2zcjuqhjz.jpeg?q=70&crop=false",
 "https://rukminim2.flixcart.com/image/832/832/xif0q/backpack/v/h/p/9-diva-19-girls-13-bkpdivagl1903-backpack-gear-41-19-original-imahybt2fs67zjgb.jpeg?q=70&crop=false",
 "https://rukminim2.flixcart.com/image/832/832/xif0q/backpack/y/g/k/9-diva-19-girls-13-bkpdivagl1903-backpack-gear-41-19-original-imahybt2gvvybmcq.jpeg?q=70&crop=false",
 "https://rukminim2.flixcart.com/image/832/832/xif0q/backpack/g/z/m/9-diva-19-girls-13-bkpdivagl1903-backpack-gear-41-19-original-imahybt2cydsrayw.jpeg?q=70&crop=false",
 "https://rukminim2.flixcart.com/image/832/832/xif0q/backpack/h/b/t/9-diva-19-girls-13-bkpdivagl1903-backpack-gear-41-19-original-imahybt2n8cqyhta.jpeg?q=70&crop=false",
 "https://rukminim2.flixcart.com/image/832/832/xif0q/backpack/l/t/g/9-diva-19-girls-13-bkpdivagl1903-backpack-gear-41-19-original-imahybt2mmzwuubh.jpeg?q=70&crop=false",

    # Add more image URLs here...
]

# Folder where you want to save the images
folder_path = "Downloads\Image"

# Create the folder if it doesn't exist
try:
    os.makedirs(folder_path, exist_ok=True)
    print(f"Folder '{folder_path}' created successfully.")
except Exception as e:
    print(f"Failed to create folder '{folder_path}'. Error: {e}")
    exit(1)

# Function to download a single image
def download_image(url, folder_path):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raises HTTPError for bad responses (4xx and 5xx)
        # Determine next available image number
        existing_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        next_image_num = len(existing_files) + 1
        filename = os.path.join(folder_path, f"image_{next_image_num}.jpg")
        print(f"Writing image {next_image_num} to file {filename}")
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"Image {next_image_num} downloaded successfully.")
    except requests.exceptions.RequestException as e:
        print(f"Failed to download image from {url}. Error: {e}")

# Download images
for url in image_urls:
    download_image(url, folder_path)
