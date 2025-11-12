from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import pymysql

url = "https://kream.co.kr"

options_ = Options()
options_.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=options_)
driver.get(url=url)
time.sleep(1)

# 돋보기 클릭-슈프림 검색-엔터
driver.find_element(By.CSS_SELECTOR, '.btn_search.header-search-button.search-button-margin').click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, '.input_search.show_placeholder_on_focus').send_keys('슈프림')
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, '.input_search.show_placeholder_on_focus').send_keys(Keys.ENTER)
time.sleep(1)

for item in range(10):
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
    time.sleep(0.5)
    
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# items = soup.select(.product_card)
# classname = '.text_body pc:w-fill pc:h-fit pc:cgap-2 pc:pt-2 tablet:w-fill tablet:h-fit tablet:cgap-2 tablet:pt-2 mo:w-fill mo:h-fit mo:cgap-2 mo:pt-2'
# classname = classname.replace(" ", ".").replace(":", "\\:")

# for item in items:
#     product_name = item.select_one(classname).text


items = soup.select('a.product_card[data-sdui-id^="product_card/"]')

product_list = []
for item in items:
    category = '상의'
    
    # 제품명 : 카드 내부, 굵지 않은 제목 & <p>태그를 갖고 있는 것
    # text-element, text-lookup, display_paragraph 세 클래스를 모두 가진 <p> 요소들 중에서 semibold 클래스가 없는(즉 굵게 처리되지 않은) 요소를 선택
    name = item.select_one('p.text-element.text-lookup.display_paragraph:not(.semibold)')
    product_name = name.get_text(strip=True) # get_text는 공백 없는 text
    # print(product_name)

    if "후드" in product_name:
        # 브랜드 : 같은 pid를 가진 별도 블록에서 굵은 <p>
        # data-sdui-id 속성이 "product_brand_name/"로 시작하는 요소 안에 포함된, semibold 클래스를 가진 <p> 요소를 선택
        brand = item.select_one('[data-sdui-id^="product_brand_name/"] p.semibold')
        product_brand = brand.get_text(strip=True)
        
        # 가격 : 
        #.price-info-container 안쪽의 .label-text-container 영역에 어디엔가 포함되어 있는 semibold 클래스를 가진 <p> 요소를 선택
        price = item.select_one('.price-info-container .label-text-container p.semibold')
        product_price = price.get_text(strip=True)
        
        # print(f"카테고리: {category}")
        # print(f"브랜드  : {product_brand}")
        # print(f"제품명  : {product_name}")
        # print(f"가격    : {product_price}")
        # print()
        
        product_info = [category, product_brand, product_name, product_price]
        product_list.append(product_info)
        
        
driver.quit()

connection = pymysql.connect(
    host = '127.0.0.1',
    user = 'root',
    passwd = 'Mretkds0401@',
    db = 'kream',
    charset = 'utf8mb4'
)

def execute_query(connection, query, args=None):
    with connection.cursor() as cursor:
        cursor.execute(query, args or ()) # select * from kream3
        if query.strip().upper().startswith("SELECT"):
            return cursor.fetchall()
        else:
            connection.commit()

for i in product_list:
    execute_query(connection, "INSERT INTO KREAM (category, brand, product_name, price) VALUES (%s, %s, %s, %s)",(i[0],i[1],i[2],i[3]))
