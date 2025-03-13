from django.shortcuts import render

# Create your views here.
def test_viwe(requast):
    name = "hamad"
    list = ["item1" , "item2" , "item" ]
    return render(requast,'test.html')
    


