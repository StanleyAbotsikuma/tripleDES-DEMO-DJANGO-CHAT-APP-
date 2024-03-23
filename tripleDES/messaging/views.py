from django.shortcuts import render

# Create your views here
def single_page(request):
    return render(request,'single_page.html')



def single_page1(request):
    return render(request,'single_page1.html')