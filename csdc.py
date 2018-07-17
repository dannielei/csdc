from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from time import sleep
from pyquery import PyQuery as pq
from selenium.common.exceptions import TimeoutException

browser=webdriver.Chrome()
wait=WebDriverWait(browser, 5)

def search():
    try:
        browser.get('http://www.chinaclear.cn/zdjs/xmzkb/center_mzkb.shtml')
        sleep(2)

        browser.switch_to_frame('frame_allA')  # 需先跳转到iframe框架

        browser.find_element_by_css_selector('#channelIdStr').click()
        browser.find_element_by_css_selector('#channelIdStr > option:nth-child(7)').click()
        sleep(2)

        next = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#form1 > div > table > tbody > tr > td:nth-child(5) > input')))
        next.click()
        sleep(2)

        browser.switch_to.default_content()
    except TimeoutException:
        return search()

def get_products():
    html=browser.page_source
    doc=pq(html)
    print(doc)

    items=doc("[style^='height']").items()
    for item in items:
        product={
            'title': item.find("[style^='border-width']").text(),
            'value': item.find("[style^='padding']").text()
        }
        print(product)

def next_page():
    try:
        browser.switch_to_frame('frame_allA')  # 需先跳转到iframe框架
        next = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div.SettlementTitle > div > a.prev')))
        next.click()
        browser.switch_to.default_content()
        sleep(2)
        get_products()
        return True
    except:
        return False


def main():

    search()
    sleep(2)
    get_products()
    print('click next page: 1')
    for i in range(2,5):
        check = next_page()
        if not check:
            break
        print('click next page: {}'.format(i))


if __name__ == '__main__':
    main()








