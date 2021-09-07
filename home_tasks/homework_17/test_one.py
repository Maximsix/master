
from selenium.webdriver import Chrome
from selenium.webdriver.remote.webelement import WebElement


def test_one():
    driver = Chrome("drivers/chromedriver")
    driver.get('https://www.jetbrains.com/')

    driver.maximize_window()

    choose_tool_selector = "//div[@class='jb-vertical-flex__grow']/p[@class][2]/a[text()='Choose your tool']"
    download_button_selector = "//a[@href='/edu-products/download/#section=idea']"
    title_ide_selector = "//p[text()='IntelliJ IDEA Edu is free & open source.'][1]"

    choose_tool: WebElement = driver.find_element_by_xpath(choose_tool_selector)
    choose_tool.click()

    driver.execute_script("window.scroll(0, 1800)")

    download_button: WebElement = driver.find_element_by_xpath(download_button_selector)
    download_button.click()

    title_ide: WebElement = driver.find_element_by_xpath(title_ide_selector)
    title_text: str = title_ide.get_attribute('innerHTML')

    assert title_text.replace('&amp;', '&') == 'IntelliJ IDEA Edu is free & open source.'

    driver.quit()

