from django.shortcuts import render

# Create your views here.
def work_view(request):
    name="ismail"
    items=["item1","item2","item3"]
    return render(request, "mytemp.html", {"name":name, "items":items})