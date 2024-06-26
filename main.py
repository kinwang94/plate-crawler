import time
import string
import random
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:\Users\Kinwang\Desktop\Chrome"


def get_plate(region: str, plate: str):
    options = Options()
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

    driver = webdriver.Chrome(options=options)
    driver.get("https://platesmania.com/us/informer")
    driver.implicitly_wait(5)

    region_dropdown = Select(driver.find_element(By.ID, "drop_1"))
    region_dropdown.select_by_visible_text(region)

    plate_input = driver.find_element(By.ID, "nomer")
    plate_input.send_keys(plate)

    # Wait until the plate type selector exists.
    _ = driver.find_element(By.ID, "myTable")

    get_button = driver.find_element(By.NAME, "Submit")
    get_button.click()

    img = driver.find_element(By.CLASS_NAME, "img-responsive")
    img_src = img.get_attribute("src")
    print(img_src)

    driver.get(img_src)

    js = """
    var elem = document.createElement('a');
    var url = '{}';
    elem.href = url;
    elem.download = '{}';
    elem.id = 'downloadAnchor';
    document.body.appendChild(elem);
    document.getElementById('downloadAnchor').click();
    """.format(img_src, plate)
    driver.execute_script(js)

    time.sleep(0.1)


def plate_gen() -> str:
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(3)) + \
           ''.join(random.choice(string.digits) for _ in range(4))


if __name__ == "__main__":
    region = "Washington"

    # for plate in ["ABC1234", "CBA4321", "AAA1111", "BBB2222", "CCC3333"]:
    #     get_plate(region, plate)

    for i in range(100):
        plate = plate_gen()
        get_plate(region, plate)
