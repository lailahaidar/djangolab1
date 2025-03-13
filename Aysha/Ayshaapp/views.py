from django.shortcuts import render

# Create your views here.
def hello(request):
    name = "Aysha"
    hello=["Aysha","Asma","lila","Ayesha"]
    return render(request,"hello.html",{"name": name, "Hello": hello})