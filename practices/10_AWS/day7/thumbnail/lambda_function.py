import os
import tempfile
import boto3
from PIL import Image
# import PIL.image

# session = boto3.Session(profile_name="ozbe15", region_name="ap-northeast-2")
session = boto3.Session(region_name="ap-northeast-2")
s3 = session.client("s3")

def lambda_handler(event, context):
    # 1) event에서 s3 정보 꺼내기
    bucket = event["Records"][0]["s3"]["bucket"]["name"]
    key = event["Records"][0]["s3"]["object"]["key"]

    # 2) s3 원본 이미지 다운로드(boto3)
    download_path = os.path.join(tempfile.gettempdir(), os.path.basename(key))
    upload_path = os.path.join(tempfile.gettempdir(), f"thumb-{os.path.basename(key)}")

    s3.download_file(bucket, key, download_path)

    # 3) 썸네일 생성(Pillow)
    with Image.open(download_path) as img:
        img.thumbnail((200, 200))
        img.save(upload_path)

    # 4) 썸네일 버킷에 업로드(boto3)
    thumbnail_bucket = bucket.replace("original", "thumbnail")
    s3.upload_file(upload_path, thumbnail_bucket, key)

    print(f"썸네일 저장 완료: s3://{thumbnail_bucket}/{key}")