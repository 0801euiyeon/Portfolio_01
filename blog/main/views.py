from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Main

def home(request):
    mains = Main.objects.all()
    return render(request, 'home.html',{'mains' : mains})

def post(request, main_id):
    main_post = get_object_or_404(Main, pk= main_id)
    return render(request, 'post.html', {'main':main_post})
    
def new(request): #new.html을 띄워주는 함수
    return render(request, 'new.html')

def create(request): #입력받은 함수를 데이터베이스에 넣어주는 함수
    main = Main()
    main.title = request.GET['title']
    main.body = request.GET['body']
    main.pub_date = timezone.datetime.now()
    main.save() #쿼리셋 메소드 위 객체들을 저장해라.
    return redirect('/post/'+str(main.id)) #문자열 형변환

def edit(request,main_id):
    main = get_object_or_404(Main, pk=main_id)
    return render(request, 'edit.html',{'main':main})

def update(request,main_id):
    main = get_object_or_404(Main, pk = main_id)
    main.title = request.GET['title']
    main.body = request.GET['body']
    main.save()
    return redirect('/post/'+str(main.id))

def delete(request, main_id):
    main = Main.objects.get(id=main_id)
    main.delete()
    return redirect('/')

# def portfolio(request,):
#     return render(requset)