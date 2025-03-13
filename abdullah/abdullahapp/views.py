from django.shortcuts import render

# Create your views here.

def example_view(request):
    variable_name = "Abdullah"
    items_list = ["Item1", "Item2", "Item3"]

    return render(request, 'test.html',{'variable_name': variable_name, 'items_list': items_list})