from django.shortcuts import render
from django.http import HttpResponse

#関数ベースビュー
#ビュー関数
def index(repuest):
    question_list = [
        "ミセスは好きですよね?",
        "もちろんハロウィン！ゾンビはお好きで？",
        "もちろんユニバ派ですよね？"
    ]
    context = {
       "question_list": question_list,
       "is_polled": True,
       "polled_msg": "投票ありがとうございました🙇",
       "not_polled_msg": "投票して下さい（圧）",
       "user_name": "UDSAJIFSAUNK!I",
    }
    return render(repuest, "main/index.html", context)