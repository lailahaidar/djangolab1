from django.shortcuts import render

# Create your views here.
def my_view(request):
    name = "BMW"
    my_list = ['M2', 'M4', 'M5']
    return render(request, 'myapp.html', {'name': name, 'my_list': my_list})