from fixtures.chrome_fixture import chrome_browser
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


def tests_wap_twitch(chrome_browser):
    chrome_browser.get("https://m.twitch.tv/")
    # Click Search Icon
    chrome_browser.find_element(By.CSS_SELECTOR, "a[aria-label='Search']").click()
    # Find StartCraft II
    input_search = chrome_browser.find_element(By.CSS_SELECTOR, "input[type='search']")
    input_search.send_keys("StarCraft II")
    chrome_browser.find_element(By.CSS_SELECTOR, "img[alt='StarCraft II']").click()
    # Scroll down 2 times 
    chrome_browser.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN*2)
    # Click a video
    videos = chrome_browser.find_elements(By.CSS_SELECTOR, "img[class='tw-image']")
    videos[len(videos)-1].click()
    # Check if video have pop up
    if chrome_browser.find_elements(By.ID, 'channel-player-gate'):
        chrome_browser.find_elements(By.CSS_SELECTOR, "div[data-a-target='tw-core-button-label-text']")[1].click() # Element 0 is "Open" button
    # Take screenshot
    sleep(4)
    chrome_browser.save_screenshot("./screenshots/test_case.png")
