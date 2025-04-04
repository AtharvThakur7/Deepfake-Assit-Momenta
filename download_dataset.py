# """
# AASIST
# Copyright (c) 2021-present NAVER Corp.
# MIT license
# """

# import os

# if __name__ == "__main__":
#     cmd = "curl -o ./LA.zip -# https://datashare.ed.ac.uk/bitstream/handle/10283/3336/LA.zip\?sequence\=3\&isAllowed\=y"
#     os.system(cmd)
#     cmd = "unzip LA.zip"
#     os.system(cmd)




# -------------------------



# Fixed Scripts 

# import os
# import zipfile
# import subprocess

# # Define dataset URL and output filename
# dataset_url = "https://datashare.ed.ac.uk/bitstream/handle/10283/3336/LA.zip?sequence=3&isAllowed=y"
# output_path = "LA.zip"
# extract_path = "ASVspoof2019_LA"

# # Use subprocess to properly handle URL in PowerShell
# print("Downloading dataset... (This may take a while)")

# try:
#     subprocess.run(
#         ["powershell", "-Command", f"Invoke-WebRequest -Uri \"{dataset_url}\" -OutFile \"{output_path}\""],
#         check=True
#     )
# except subprocess.CalledProcessError:
#     print("Download failed! Check your internet connection and try again.")
#     exit(1)

# # Verify if file exists and is not empty
# if not os.path.exists(output_path) or os.path.getsize(output_path) < 10000000:  # Check if file is too small (corrupt)
#     print("Download failed or file is incomplete! Try downloading again.")
#     exit(1)

# # Extract dataset using Python's zipfile module
# print("Extracting dataset...")
# try:
#     with zipfile.ZipFile(output_path, 'r') as zip_ref:
#         zip_ref.extractall(extract_path)
#     print(f"Dataset extracted to {extract_path} successfully!")
# except zipfile.BadZipFile:
#     print("Error: The downloaded zip file is corrupted. Try downloading again.")
#     exit(1)



import os
import zipfile
import requests
import sys

# Define dataset URL and output filename
dataset_url = "https://datashare.ed.ac.uk/bitstream/handle/10283/3336/LA.zip?sequence=3&isAllowed=y"
output_path = "LA.zip"
extract_path = "ASVspoof2019_LA"

# Function to download file reliably
def download_file(url, output_path):
    print("Downloading dataset... (This may take a while)")
    try:
        with requests.get(url, stream=True) as response:
            response.raise_for_status()  # Check for HTTP errors
            with open(output_path, "wb") as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
        print("Download complete!")
    except requests.exceptions.RequestException as e:
        print(f"Download failed: {e}")
        sys.exit(1)

# Step 1: Download dataset using requests
download_file(dataset_url, output_path)

# Step 2: Check if the file exists and is not empty
if not os.path.exists(output_path) or os.path.getsize(output_path) < 10000000:
    print("Download failed or file is incomplete! Check your internet connection and try again.")
    sys.exit(1)

# Step 3: Extract dataset using Python's zipfile module
print("Extracting dataset...")
try:
    with zipfile.ZipFile(output_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)
    print(f"✅ Dataset extracted to {extract_path} successfully!")
except zipfile.BadZipFile:
    print("❌ Error: The downloaded zip file is corrupted. Try downloading again.")
    sys.exit(1)
