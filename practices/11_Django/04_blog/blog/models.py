from django.db import models

class Blog(models.Model):
    # author
    CATEGORY_CHOICES = {
        ('free','자유'),
        ('travel','여행'),
        ('pet','반려동물'),
        ('investing','투자'),
    }
    category = models.CharField(max_length = 15, choices = CATEGORY_CHOICES)
    title = models.CharField(max_length=100)
    content = models.TextField()

    created_at = models.DateTimeField('작성일자',auto_now_add=True)
    updated_at = models.DateTimeField('수정일자',auto_now=True)

    def __str__(self):
        return f'[{self.get_category_display()}] {self.title}'

    class Meta:
        verbose_name = '블로그'
        verbose_name_plural = '블로그 목록'
