from django.shortcuts import render

# Create your views here.
def my_view(request):

    name = 'yousef'
    myl = ['1', '2', '3', '4']
    return render (request, 'mytemplate.html')
    #return render(request, "mytemplate.html", {'name': name, 'myl': myl})