import os
import time
import shutil
import requests
from random import randrange
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


def FillElem(drv, selector, value):
    temp = drv.find_elements_by_css_selector(selector)
    if len(temp) > 0:
        temp[0].send_keys(value)


def WaitTillElementCome(drv, selector, count=10, seconds=1):
    counter = 0
    time.sleep(seconds)
    element = drv.find_elements_by_css_selector(selector)
    while len(element) < 0 and counter < count:
        time.sleep(seconds)
        element = driver.find_elements_by_css_selector(selector)
        counter += 1


def login(drv):
    WaitTillElementCome(drv, "input[name='username']")
    FillElem(drv, "input[name='username']", "forfakeiko")
    FillElem(drv, "input[name='password']", "13579F2468fi")
    drv.find_element_by_css_selector("button[type='submit']").click()
    WaitTillElementCome(drv, "img[data-testid='user-avatar']")


def save_image_to_file(imageUrl, name):
    if not os.path.isdir("img"):
        os.mkdir("img")
    response = requests.get(imageUrl, stream=True)
    with open('{}/{}'.format("img", name), 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)


# opens instagram
driver = webdriver.Firefox()
driver.get("https://www.instagram.com")

# fills account infos
login(driver)
time.sleep(1)
username_field = list(driver.find_elements_by_css_selector("input[name='username']"))
if len(username_field):
    login(driver)

# goto explore
driver.get("https://www.instagram.com/explore/")

# clik random image
WaitTillElementCome(driver, "[role='main']")
images = list(driver.find_elements_by_css_selector("img"))
while len(images) < 5:
    time.sleep(1)
    images = list(driver.find_elements_by_css_selector("img"))

random_image = images[randrange(10)]
random_image.find_element_by_xpath("..").find_element_by_xpath("..").find_element_by_xpath(
    "..").find_element_by_xpath("..").find_element_by_xpath("..").click()
time.sleep(1)

video = list(driver.find_elements_by_css_selector("article video"))
while len(video):
    video[0].send_keys(Keys.ESCAPE)
    random_image = images[randrange(10)]
    random_image.find_element_by_xpath("..").find_element_by_xpath("..").find_element_by_xpath(
        "..").find_element_by_xpath("..").find_element_by_xpath("..").click()
    time.sleep(1)
    video = list(driver.find_elements_by_css_selector("article video"))


WaitTillElementCome(driver, "article img[alt*='Photo by']")
full_image_elements = list(driver.find_elements_by_css_selector("article img[alt*='Photo by']"))

for full_image in full_image_elements:
    src = full_image.get_attribute("src")
    save_image_to_file(src, "test")
