from django.shortcuts import render

# Create your views here.
def test_view(request):
    name="seyed"
    list=[1,2,3,4,5]
    context = {
        'name': name,
        'list': list,
    }

    return render(request, 'templates.html', context)