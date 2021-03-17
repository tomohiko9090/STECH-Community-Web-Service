from django.db import models

# Create your models here.
class BoardModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    auther = models.CharField(max_length=100)
    snsimage = models.ImageField(upload_to='')#どこにuploadするか
    # null→DB関係　DBにnullが入ってきても問題ないよ
    # blank→入力されたフォーム関係 フォームで入力されずgoodやreadが入力されなくてもエラーにならないよ
    # default→何も入っていない時に自動で入力されるもの

    good = models.IntegerField(null=True, blank=True, default=1)
    read = models.IntegerField(null=True, blank=True, default=1)
    readtext = models.TextField(null=True, blank=True, default='a')
    #readtextでは1ユーザ１回のみ既読カウントする

from django.conf import settings

class Item(models.Model):
    title = models.CharField(max_length=100)
    
    category = models.CharField(max_length = 100)
    slug = models.SlugField()
    description = models.TextField()
    

    def __str__(self):
        return self.title
# Create your models here.

class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    
    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_total_item_price()
        return total

    def __str__(self):
        return self.user.email