from django.shortcuts import render

# Create your views here.
def work_view(request):
    name='mohammad'
    cars=['dodge', 'bm', 'Toyota']
    return render(request, 'mytemp.html', {"name":name, "cars":cars})