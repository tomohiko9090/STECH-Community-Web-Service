from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from .models import BoardModel
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Create your views here.

#requestにはmethodを筆頭にいろんな情報が入ってくる
#methodでpostとgetに分けることで分岐を作りたい

def signupfunc(request):
    if request.method == 'POST':
        username2 = request.POST['username']#DBからデータ項目、インデックスを引っ張り出すイメージ
        password2 = request.POST['password']
        #signupで重複した際、エラー表示
        try:#新規登録した時にアカウントがすでに存在している場合
            User.objects.get(username=username2)
            return render(request, 'signup.html', {'error':'このユーザは既に存在しているわ。他のにして頂戴。'})
        except:#存在していない場合
            user = User.objects.create_user(username2, '', password2)#ここで初めて新規アカウントが作られる！
            ## 【変更箇所：高橋】
            ## return render(request, 'signup.html', {'some':100})
            return redirect('login')
    #functionを使う場合は、renderでtemplate(引数2)とDB(引数3)を組み合わせる
    return render(request, 'signup.html', {'some':100})
    
#logninした時の場合の表示を作っていく
def loginfunc(request):
    if request.method == 'POST':
        username2 = request.POST['username']
        password2 = request.POST['password']
        user = authenticate(request, username=username2, password=password2)
        if user is not None:#そのユーザがいる場合はログイン処理をする
            login(request, user)
            return redirect('list')
        else:#いない場合は
            return render(request, 'login.html', {})
    return render(request, 'login.html', {})

#@login_required#関数が実行される前に、ログインを確認
def listfunc(request):
    object_list = BoardModel.objects.all()
    return render(request, 'list.html', {'object_list':object_list})

def logoutfunc(request):
    logout(request)
    return redirect('login')

def detailfunc(request, pk):#pkでリスト番号をとってくる
    object = get_object_or_404(BoardModel, pk=pk)
    return render(request, 'detail.html', {'object':object})

def goodfunc(request, pk):
    object = BoardModel.objects.get(pk=pk)
    object.good = object.good + 1
    object.save()
    return redirect('list')

def readfunc(request, pk):
    object = BoardModel.objects.get(pk=pk)
    username = request.user.get_username()
    if username in object.readtext:#すでに既読している場合
        return redirect('list')
    else:
        object.read = object.read + 1
        object.readtext = object.readtext + ' ' + username #スペースありで人を格納していく、同じ名前があったらその時点でアウト
        object.save()
        return redirect('list')

class BoardCreate(CreateView):
    template_name = 'create.html'
    model = BoardModel
    fields = ('title', 'content', 'auther', 'snsimage')#記入する内容
    success_url = reverse_lazy('list')#データが作成した後に遷移させる

def like_listfunc(request):
    object_list = BoardModel.objects.all()
    return render(request, 'like_list.html', {'object_list':object_list})

def chat_listfunc(request):
    object_list = BoardModel.objects.all()
    return render(request, 'chat_list.html', {'object_list':object_list})