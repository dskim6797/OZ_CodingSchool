import boto3
import os
from botocore.exceptions import ClientError

session = boto3.Session(profile_name="ozbe15")
s3 = session.client("s3")
# s3.create_bucket(Bucket="ozbe15-boto3-dskim", CreateBucketConfiguration={"LocationConstraint":"ap-northeast-2"})


def upload_api():
    # 1) 사용자로부터 업로드 할 파일 경로 입력
    file_path = input("업로드 할 파일 경로를 입력하세요: ").strip()
    
    # 2) 파일 경로 유효성 검사
    if not os.path.isfile(file_path):
        print("파일 경로가 올바르지 않습니다.")
        return
    
    # 3) S3 버킷에 파일 업로드
    bucket_name = "ozbe15-boto3-dskim"
    object_name = os.path.basename(file_path)
    try:
        s3.upload_file(file_path, bucket_name, object_name)
        print(f"파일이 S3 버킷 '{bucket_name}'에 업로드되었습니다: {object_name}")
    except ClientError as e:
        print(f"파일 업로드 중 오류가 발생했습니다: {e}")
        return
    


if __name__ == "__main__":
    upload_api()