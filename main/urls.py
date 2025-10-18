# path関数をインポート
from django.urls import path

# views.pyをインポート
from . import views

urlpatterns = [
    path("", views.index, name = "index"), # viewsのindex関数を呼び出す
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]