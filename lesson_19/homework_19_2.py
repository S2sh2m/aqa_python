import requests

BASE_URL = "http://127.0.0.1:8080"

with open(r"C:\Users\pc-551\PycharmProjects\aqa_python\lesson_19\example.jpg", "rb") as img:
    files = {"image": img}
    upload_response = requests.post(f"{BASE_URL}/upload", files=files)

image_url = upload_response.json().get("image_url")
filename = image_url.split("/")[-1]

get_response = requests.get(f"{BASE_URL}/image/{filename}", headers={"Content-Type": "text"})

delete_response = requests.delete(f"{BASE_URL}/delete/{filename}")

print("Upload:", upload_response.status_code)
print("Get:", get_response.status_code)
print("Delete:", delete_response.status_code)