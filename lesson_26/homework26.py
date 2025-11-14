from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://localhost:8000/dz.html")

frames = [
    ("frame1", "input1", "Frame1_Secret"),
    ("frame2", "input2", "Frame2_Secret")
]

for frame_id, input_id, secret_text in frames:

    frame = driver.find_element(By.ID, frame_id)
    driver.switch_to.frame(frame)

    driver.find_element(By.ID, input_id).send_keys(secret_text)

    driver.find_element(By.TAG_NAME, "button").click()

    alert = driver.switch_to.alert
    alert_text = alert.text
    print(f"[{frame_id}] Alert text:", alert_text)

    assert alert_text == "Верифікація пройшла успішно!"

    alert.accept()

    driver.switch_to.default_content()

time.sleep(2)
driver.quit()
