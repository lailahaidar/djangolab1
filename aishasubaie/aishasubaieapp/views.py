from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def student(request):
    name = 'Aisha'
    students= ['Aisha', 'Sara', 'Nora', 'Lama']
    return render(request, 'student.html', {'name':name, 'students':students})
