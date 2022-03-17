from django.shortcuts import render
from friendship.models import QuizUser,Ques
import random
# Create your views here.

def create_user(request,username=None):
    return render(request, "login.html", {"name":username})

def play_quiz(request,username= None):
    if request.POST['name']:
        if username == 'None': 
            user = QuizUser.objects.create(name=request.POST['name'])
            questions = list(Ques.objects.all())
            questions  = random.sample(questions, 10)
            for quest in questions:
                quest.quiz_user = user
                quest.save()
            return render(request,"testPage.html",{'questions':questions,'name': request.POST['name']})
        else:
            questions = Ques.objects.filter(quiz_user__name = username)
            return render(request,"testPage.html",{'questions':questions,'name': request.POST['name'],"friend":username})
    return render(request,"404.html",{})                

def submit(request,username,friend=None):
    if request.POST:
        count = 0
        if str(friend) != 'None':
            percentage = 0
            questions = Ques.objects.filter(quiz_user__name = username)
            for ques,value in (request.POST).items():
                 if count>0:
                    check = list(questions.filter(question = ques))
                    if check and check[0].ans == value:
                        percentage += 10
                 count +=1
            return render(request,"percentage.html",{'percentage':percentage})                
        else:
            for ques,value in (request.POST).items():
                if count>0:
                    Ques.objects.filter(quiz_user__name = username,question=ques).update(ans=value)
                count = count + 1
            link="http://127.0.0.1:8000/register/" + username
            return render(request,'shareLink.html',{'link':link})
    return render(request,"404.html",{})
