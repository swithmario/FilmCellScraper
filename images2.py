import os
import pandas as pd
import requests

def download_image(image_url, output_folder):
    try:
        # Get image content
        response = requests.get(image_url)
        if response.status_code == 200:
            # Generate file name
            image_name = "image_817.png"  # Fixed name for the 817th image
            # Save image to file
            with open(os.path.join(output_folder, image_name), 'wb') as f:
                f.write(response.content)
            print("Image downloaded successfully.")
        else:
            print(f"Failed to download image. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error downloading image: {e}")

# Usage example
csv_file = 'ebrn.csv'
output_folder = 'downloaded_images'

# Read the CSV file into a list
with open(csv_file, 'r') as f:
    csvlist = f.readlines()

# Get the 817th image URL from the list
image_817_url = csvlist[817].strip()

# Download the 817th image
download_image(image_817_url, output_folder)
