from django.urls import path
from . import views


urlpatterns = [
    path("", views.memo_list, name="memo_list"),
    path("<int:pk>/", views.memo_detail, name="memo_detail"),
    path("create/", views.memo_create, name="memo_create"),
    path("<int:pk>/update/", views.memo_update, name="memo_update"),
    path("<int:pk>/delete/", views.memo_delete, name="memo_delete"),
]
