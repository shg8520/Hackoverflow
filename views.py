from django.http import HttpRequest
from django.shortcuts import render
import joblib

def index(request):
    return render(request,'index.html')

def result(request):
    cls=joblib.load('model.sav')
    lis=[]
    lis.append(request.GET['Gender'])
    lis.append(request.GET['Age'])
    lis.append(request.GET['Activity'])
    lis.append(request.GET['Fitness_level'])
    lis.append(request.GET['whpd'])
    lis.append(request.GET['exdaily'])
    lis.append(request.GET['papd'])
    lis.append(request.GET['diet_plans'])
    lis.append(request.GET['sleep'])
    lis.append(request.GET['famfr'])
    lis.append(request.GET['ent'])
    lis.append(request.GET['socmed'])
    lis.append(request.GET['stress'])
    lis.append(request.GET['mentalhealth'])

    ans=cls.predict([lis])
    if(ans==[1]):
        res="You could try some Zumba exercise or try some Yoga poses like Surya Namaskara ,Vajrasana,etc.\n You could also try meditations which calm your mind like progressive relaxation and visualization meditation."
    if(ans==[2]):
        res="You could try some Zumba exercise or try some Yoga poses like Surya Namaskara,Vajrasana ,etc.\n You could also listen to motivational podcast and try trancendental meditation."
    if(ans==[3]):
        res="You could try some Zumba exercise or try some Yoga poses like Surya Namaskara,Vajrasana ,etc.Try meditating daily."
    if(ans==[4]):
        res="You could try Bokwa or try yoga poses like Surya namaskara,Virabhadra III and if you want to you can do cardio/swimming etc.You could do progressive relaxation and visualization meditation."
    if(ans==[5]):
        res="You could try Bokwa or try yoga poses like Surya namaskara,Virabhadra III and if you want to you can do cardio/swimming etc.You could also listen to motivational podcast and try trancendental meditation."
    if(ans==[6]):
        res="You could try Bokwa or try yoga poses like Surya namaskara,Virabhadra III and if you want to you can do cardio/swimming etc.Try meditating daily."
    if(ans==[7]):
        res="Keep up with your good work and Try some yoga poses like Surya Namaskara,etc.You could also try meditations which calm your mind like progressive relaxation and visualization meditation."
    if(ans==[8]):
        res="Keep up with your good work and Try some yoga poses like Surya Namaskara,etc.You could also listen to motivational podcast and try trancendental meditation."
    if(ans==[9]):
        res="Keep up with your good work and Try some yoga poses like Surya Namaskara,etc.Try meditating daily."
    return render(request,'result.html',{'lis':lis,'ans':ans,'res':res})
