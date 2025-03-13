from django.shortcuts import render

# Create your views here.
def test_view(request):
    name = "Abdo"
    my_list = ["cars", "houses", "planes"]
    return render(request, 'test.html', {'name': name, 'my_list': my_list})