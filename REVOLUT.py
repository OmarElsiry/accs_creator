from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import time

# Specify the user data directory and profile directory
user_data_dir = f"C:\\Users\\PotterParker\\AppData\\Local\\Google\\Chrome\\User Data"

profile_directory = (
    f"Profile 1"  # Change this to the desired profile directory name   # default
)
# Create Chrome options with user data and profile directory
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.49"
)
chrome_options.add_argument("--incognito")  # Start Chrome in incognito mode
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
chrome_options.add_argument(f"--profile-directory={profile_directory}")
chrome_options.add_argument(
    "--start-minimized"
)  # Add this line to start Chrome maximized

driver = webdriver.Chrome(
    options=chrome_options
)  # Optional argument, if not specified will search path.
driver.get("https://www.revolut.com/")

numbers_list = [
    "400029553",
    "400031333",
    "400263728",
]

counter = 0

for number in numbers_list:
    try:
        WebDriverWait(driver, 1).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[2]/div/div/div[1]/button[2]/span[2]")
            )
        ).click()

    except TimeoutException:
        print("Button not found, continuing...")

    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, "/html/body/div/header/div/div[1]/span/div/span/a[2]/span[2]")
        )
    ).click()

    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "/html/body/div[2]/div/div/div/div[2]/form/span/label[2]/div/span/span[1]/input",
            )
        )
    ).send_keys(number)
    print("Number: " + number + " is done")

    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "/html/body/div[2]/div/div/div/div[2]/form/span/label[1]/div/span/span[1]/input",
            )
        )
    ).click()

    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "/html/body/div[4]/div/div[1]/div[1]/span/div[1]/div/input",
            )
        )
    ).send_keys("azerbijan")

    time.sleep(2.5)

    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "/html/body/div[4]/div/div[1]/div[2]/div/div/button/div/span/span/span[1]",
            )
        )
    ).click()

    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "/html/body/div[2]/div/div/div/div[2]/form/button[2]/span[2]/span",
            )
        )
    ).click()
    counter += 1

    time.sleep(7)

    if counter == 25:
        print("counter = " + str(counter) + "\n" + "Waiting temp Ban to end")
        time.sleep(900)
        counter = 0
        ActionChains(driver).key_down(Keys.CONTROL).send_keys("r").key_up(
            Keys.CONTROL
        ).perform()
        time.sleep(1)  # Wait for the page to refresh
        driver.delete_all_cookies()  # Delete all cookies
        print("counter = " + str(counter) + "\n")
        time.sleep(10)
