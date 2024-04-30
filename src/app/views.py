from django.shortcuts import render

# Create your views here.
def barcode(request):
    return render(request,'barcode.html')