from django.db import models

# Create your models here.
class BoardModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    auther = models.CharField(max_length=100)
    snsimage = models.ImageField(upload_to='')
    birthday = models.DateField()
    # null→DB関係　DBにnullが入ってきても問題ないよ
    # blank→入力されたフォーム関係 フォームで入力されずgoodやreadが入力されなくてもエラーにならないよ
    # default→何も入っていない時に自動で入力されるもの

    good = models.IntegerField(null=True, blank=True, default=1)
    read = models.IntegerField(null=True, blank=True, default=1)
    readtext = models.TextField(null=True, blank=True, default='a')
    #readtextでは1ユーザ１回のみ既読カウントする