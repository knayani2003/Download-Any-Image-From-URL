import os
from urllib.parse import urljoin
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import logging

def setup_logging():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def download_images_from_url(url, folder_path):
    """
    Download all images from the specified webpage URL and save them to the specified folder path.
    
    Parameters:
        url (str): The URL of the webpage to download images from.
        folder_path (str): The local directory path to save the downloaded images.
    """
    setup_logging()
    
    logging.info("Initializing the WebDriver...")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get(url)

    # Extract all image URLs from the webpage
    image_urls = []
    images = driver.find_elements(By.TAG_NAME, "img")
    for img in images:
        src = img.get_attribute('src')
        if src:
            img_url = urljoin(url, src)
            image_urls.append(img_url)
    
    if not image_urls:
        logging.warning("No images found on the webpage.")
        driver.quit()
        return

    # Create the folder if it doesn't exist
    try:
        os.makedirs(folder_path, exist_ok=True)
        logging.info(f"Folder '{folder_path}' created successfully.")
    except Exception as e:
        logging.error(f"Failed to create folder '{folder_path}'. Error: {e}")
        driver.quit()
        return

    # Determine the starting index for new images
    existing_files = os.listdir(folder_path)
    existing_image_numbers = [
        int(f.split('_')[1].split('.')[0]) 
        for f in existing_files if f.startswith('image_') and f.endswith('.jpg')
    ]
    start_index = max(existing_image_numbers, default=0) + 1

    # Download each image
    for i, img_url in enumerate(image_urls, start=start_index):
        try:
            response = requests.get(img_url, timeout=10)
            response.raise_for_status()
            filename = os.path.join(folder_path, f"image_{i}.jpg")
            with open(filename, 'wb') as f:
                f.write(response.content)
            logging.info(f"Image {i} downloaded successfully.")
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to download image from {img_url}. Error: {e}")

    # Quit the WebDriver
    driver.quit()

if __name__ == "__main__":
    url = input("Enter the webpage URL: ")
    folder_path = "Downloads/Image"
    download_images_from_url(url, folder_path)
