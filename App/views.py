from django.shortcuts import render
from .forms import BildenForm
from .models import Bildens_model

# Create your views here.
def getIndex(request):
    form = BildenForm()
    return render (request, 'index.html', {'form':form})
   

def save_form(request):
    
    data ={
        'form':BildenForm()
    }
    if request.method == 'POST':
        bild = BildenForm(data=request.POST)
        if bild.is_valid():
            bild.save()
        else:
            data['form'] = bild
      
    return render(request, 'success.html', data)
    
    
    
    
    # if request.method == 'POST':
    #     try:
    #         fot = request.FILES['txtfot']
    #     except:
    #         fot = 'media/Firma_6.png'
    #     canv = Bildens_model( imagen=fot)
    #     canv.save()
        
    #     return render(request, 'success.html')
    # else:
    #     return render(request, 'success.html')
