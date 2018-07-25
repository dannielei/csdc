from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.common.exceptions import TimeoutException

browser=webdriver.Chrome()
wait=WebDriverWait(browser, 5)

def search():
    try:
        browser.get('http://www.chinaclear.cn/zdjs/xmzkb/center_mzkb.shtml')
        sleep(2)

        browser.switch_to_frame('frame_allA')  # 需先跳转到iframe框架

        browser.find_element_by_css_selector('#channelIdStr').click()
        browser.find_element_by_css_selector('#channelIdStr > option:nth-child(6)').click()#选择类型
        sleep(2)

        next = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#form1 > div > table > tbody > tr > td:nth-child(5) > input')))
        next.click()#查询
        sleep(2)

        get_products()

        browser.switch_to.default_content()#跳出iframe框架

    except TimeoutException:
        return search()

def get_products():
    a = browser.find_element_by_css_selector('body > div.SettlementTitle > h2')  # 定位时间区间
    print(a.text)

    t = browser.find_element_by_xpath('//*[@id="settlementList"]/table/tbody/tr/td/table/tbody')  # 定位表格
    table_rows = len(t.find_elements_by_tag_name('tr'))
    table_cols = len((t.find_elements_by_tag_name('tr'))[0].find_elements_by_tag_name('td'))
    for rows in range(1,table_rows):
        for cols in range(1,table_cols):
            # print({'b':(rows+1,1),'c':(1, cols+1),'d':(rows+1, cols+1)})
            b = browser.find_element_by_css_selector('#settlementList > table > tbody > tr > td > table > tbody > tr:nth-child({}) > td:nth-child({}) > p'.format(rows+1,1))
            c = browser.find_element_by_css_selector(
            '#settlementList > table > tbody > tr > td > table > tbody > tr:nth-child({}) > td:nth-child({}) > p'.format(1, cols+1))
            d = browser.find_element_by_css_selector(
            '#settlementList > table > tbody > tr > td > table > tbody > tr:nth-child({}) > td:nth-child({}) > p'.format(rows+1, cols+1))
            e={b.text+'/'+c.text:d.text}
            print(e)

def next_page():
    try:
        browser.switch_to_frame('frame_allA')  # 需先跳转到iframe框架
        next = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div.SettlementTitle > div > a.prev')))
        next.click()
        sleep(2)
        get_products()
        browser.switch_to.default_content()
        return True
    except:
        return False

def main():
    search()
    sleep(2)
    print('click next page: 1')
    for i in range(2,2):
        check = next_page()
        if not check:
            break
        print('click next page: {}'.format(i))

if __name__ == '__main__':
    main()
