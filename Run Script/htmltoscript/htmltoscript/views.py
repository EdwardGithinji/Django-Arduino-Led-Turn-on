from django.shortcuts import render, render_to_response
import requests
from .ledonoff import Led_onoff
from .forms import SearchForm
#def button(request):
#    return render(request,'home.html')

def outputon(request):
    if request.method=='GET':
        turn=Led_onoff('1')
        On=turn.led_on()


    #return render_to_response(request,)
    #print('shsjsjs')
    #context = {'data':turn.led_on()}
    #on=requests.post(name='scripton')
    return render(request,'home.html')
    # data=requests.get("https://regres.in/api/users")
    #
    # print(data.text)
    # data=data.text
    # return render(request,'home.html',{'data':data})

def outputoff(request):
    if request.method=='GET':
        turn=Led_onoff('0')
        Off=turn.led_off()
#     off = requests.post(name='scriptoff')
#     #context = {'data':turn.led_off()}
    return render(request,'home.html')