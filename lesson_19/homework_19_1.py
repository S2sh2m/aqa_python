import os
import requests

API_KEY = "L6dsMFmbmztX6fqlVFIe0ZYtl03C2NgyO5f0NDF6"
URL = "https://api.nasa.gov/mars-photos/api/v1/rovers/perseverance/latest_photos"
params = {"api_key": API_KEY}

response = requests.get(URL, params=params, timeout=15)

if response.status_code != 200:
    print(response.text)
    exit()

data = response.json()
photos = data.get("latest_photos", [])

if not photos:
    print("No photo")
    exit()

os.makedirs("mars_photos", exist_ok=True)

for i, photo in enumerate(photos[:5], start=1):
    img_url = photo["img_src"]
    filename = f"mars_photos/mars_photo{i}.jpg"

    img_data = requests.get(img_url, timeout=15).content
    with open(filename, "wb") as f:
        f.write(img_data)