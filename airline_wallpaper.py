import os
import time
import struct
import ctypes
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException
import random

# Configure Chrome options
chrome_options = Options()
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_argument("--headless")

# Create a Chrome driver
driver_path = "YOUR_CHROMEDRIVER_PATH"
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Set page load timeout
driver.set_page_load_timeout(10)

# Load a random photo page from JetPhotos
t = time.time()
try:
    photo_id = random.randint(10844358, 10864383)
    driver.get(f"https://www.jetphotos.com/photo/{photo_id}")
except TimeoutException:
    driver.execute_script("window.stop();")
    print('Time consuming:', time.time() - t)

# Get the image source URL
photo = driver.find_element(By.XPATH,"/html/body/div[1]/main/section/div[4]/div/div[2]/a/img")
img_src = photo.get_attribute('src')

# Print the image source URL
print(img_src)

# Download and save the image
WALLPAPER_PATH = 'YOUR_WALLPAPER_PATH'
photo.screenshot(WALLPAPER_PATH)

# Set the downloaded image as the wallpaper
SPI_SETDESKWALLPAPER = 20
def is_64_windows():
    return struct.calcsize('P') * 8 == 64

def get_sys_parameters_info():
    return ctypes.windll.user32.SystemParametersInfoW if is_64_windows() \
        else ctypes.windll.user32.SystemParametersInfoA

def change_wallpaper():
    sys_parameters_info = get_sys_parameters_info()
    r = sys_parameters_info(SPI_SETDESKWALLPAPER, 0, WALLPAPER_PATH, 0)
    if not r:
        print(ctypes.WinError())

change_wallpaper()

# Quit the driver
driver.quit()
