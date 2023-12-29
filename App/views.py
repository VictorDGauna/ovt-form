from django.shortcuts import render
from .forms import BildenForm
from .models import Bildens_model

# Create your views here.
def getIndex(request):
    form = BildenForm()
    return render (request, 'index.html', {'form':form})
   

def save_form(request):
    if request.method == 'POST':
        form = BildenForm(request.POST, request.FILES)
        if form.is_valid():
           form.save()
    
    return render(request, 'templates/success.html',{'form':form})
    