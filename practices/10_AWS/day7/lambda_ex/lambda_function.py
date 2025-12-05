import json
import requests
from bs4 import BeautifulSoup

def lambda_handler(event, context):
    #) HTTP 요청
    response = requests.get("https://www.example.com/")
    print(response.text)

    # 2) html -> bs4 파싱
    soup = BeautifulSoup(response.text, "html.parser")

    # 3) bs4 객체 데이터 추출
    h1_tags = []
    for tag in soup.find_all("h1"):
        h1_tags.append(tag.text)

    return {
        "statusCode": 200,
        "body": json.dumps(h1_tags)
    }