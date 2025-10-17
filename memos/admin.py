from django.contrib import admin
from .models import Memo


@admin.register(Memo)
class MemoAdmin(admin.ModelAdmin):
    """메모 관리자"""
    list_display = ["title", "user", "created_at", "updated_at"]
    list_filter = ["created_at", "updated_at"]
    search_fields = ["title", "content"]
