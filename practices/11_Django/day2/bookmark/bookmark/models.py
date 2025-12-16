from django.db import models

# Model = DB의 테이블
# Field = DB의 컬럼

# makemigrations => migration.py 파일을 만든다
# 실제 DB에는 영향 X, DB에 넣기 위한 정의를 하는 파일을 생성

# migrate => migrations/ 폴더 안에 있는 migration 파일들을 실제 DB에 적용함

# makemigrations - DB에 적용 x, 적용할 파일 생성 (like git의 commit)
# migrate - migrations 파일 기록을 가지고 DB에 적용 O (like git의 push)


class Bookmark(models.Model):
    name = models.CharField('이름',max_length=100)
    url = models.URLField('URL',max_length=100)
    created_at = models.DateTimeField('생성 일시',auto_now_add=True)
    updated_at = models.DateTimeField('수정 일시',auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '북마크'
        verbose_name_plural = '북마크 목록'
