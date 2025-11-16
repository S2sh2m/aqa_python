from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_nova_poshta_tracking():
    driver = webdriver.Chrome()
    driver.maximize_window()

    ttn = "20450123456789"
    expected_status = ("Ми не знайшли посилку за таким номером. "
                       "Якщо ви шукаєте інформацію про посилку, якій більше 3 місяців, будь ласка, "
                       "зверніться у контакт-центр: 0 800 500 609")

    driver.get("https://tracking.novaposhta.ua/#/uk")

    input_field = driver.find_element(By.CSS_SELECTOR, "input[type='text']")
    input_field.send_keys(ttn)

    time.sleep(2)

    search_btn = driver.find_element(By.ID, "np-number-input-desktop-btn-search-en")
    search_btn.click()
    time.sleep(2)

    status = driver.find_element(By.ID, "np-number-input-desktop-message-error-message").text
    print("Status:", status)

    assert status == expected_status

    driver.quit()


if __name__ == "__main__":
    test_nova_poshta_tracking()
