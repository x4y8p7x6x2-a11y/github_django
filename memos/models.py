from django.db import models
from django.contrib.auth.models import User


class Memo(models.Model):
    """메모 모델"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="memos")
    title = models.TextField("제목")
    content = models.TextField("내용")
    created_at = models.DateTimeField("생성일", auto_now_add=True)
    updated_at = models.DateTimeField("수정일", auto_now=True)

    class Meta:
        db_table = "memos"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
