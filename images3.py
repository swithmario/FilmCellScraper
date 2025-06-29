import os
import pandas as pd
import requests

def download_images(csv_file, output_folder):
    # Read CSV file
    with open(csv_file, 'r') as f:
        # Read lines
        image_urls = f.readlines()

    # Create output folder if not exists
    os.makedirs(output_folder, exist_ok=True)

    # Iterate over image URLs
    for index, image_url in enumerate(image_urls):
        image_url = image_url.strip()  # Remove leading/trailing whitespace
        try:
            # Get image content
            response = requests.get(image_url)
            if response.status_code == 200:
                # Generate file name
                image_name = f"image_{index}.png"
                # Save image to file
                with open(os.path.join(output_folder, image_name), 'wb') as f:
                    f.write(response.content)
                print(f"Image {index} downloaded successfully.")
            else:
                print(f"Failed to download image {index}. Status code: {response.status_code}")
        except Exception as e:
            print(f"Error downloading image {index}: {e}")

# Usage example
csv_file = 'ebay_image_links.csv'
output_folder = 'downloaded_images'
download_images(csv_file, output_folder)
