from django.shortcuts import render

# Create your views here.

def lab_view(request):
    x = "abdulrahman"
    mylist = ['saad', 'ahmed', 'ali']
    return render(request,'lab.html',{'name': x}, {'mylist': mylist})
