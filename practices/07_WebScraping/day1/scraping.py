import requests
from bs4 import BeautifulSoup

keyword = input('검색어를 입력해주세요 : ')
url = 'https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query=' + keyword

rep = requests.get(url)
# print(rep)
# print(rep.text)

html = rep.text
soup = BeautifulSoup(html, 'html.parser') # html에서 사용된 모든 태그의 유형을 알려주줌

result = soup.select('.sds-comps-vertical-layout.sds-comps-full-layout.IoSVvu2hEbI_In6t6FAw')


for i in result:
    # 광고와 관련된 태그 거르기
    ad = i.select_one('.vZ_ErVj5n5d07m6XzhoL') # 광고 아닐때 None
    if not ad:
        # 추출하기 - 링크, 제목, 작성자, 요약
        title = i.select_one('.sds-comps-text.sds-comps-text-ellipsis.sds-comps-text-ellipsis-1.sds-comps-text-type-headline1.sds-comps-text-weight-sm').text
        writer = i.select_one('.sds-comps-text.sds-comps-text-ellipsis.sds-comps-text-ellipsis-1').text
        dsc = i.select_one('.sds-comps-text.sds-comps-text-type-body1.sds-comps-text-weight-sm').text
        dsc = i.select_one('.sds-comps-text.sds-comps-text-type-body1.sds-comps-text-weight-sm').text
        link = i.select_one('.ialLiYPc7XEN3dJ4Tujv.pHHExKwXvRWn4fm5O0Hr')['href']
        print(f"제목 : {title}")
        print(f"작성자 : {writer}")
        print(f"요약 : {dsc}")
        print(f"링크 : {link}")






