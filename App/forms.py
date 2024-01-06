from django import forms
from .models import Bildens_model
# from django.core.validators import RegexValidator

class BildenForm(forms.ModelForm):
    
    class Meta:
        model = Bildens_model
       
        
        fields = '__all__'
        MARITAL = [('Single','Single'),('Married','Married'),('Other','Other')]
       
        
        widgets ={
            'who':forms.Textarea(attrs={'id':'who','name':'who','autofocus':'true','required':'true'} ),
            'creditEnrichment':forms.Textarea(attrs={'id':'reffered'} ),
            'dateOfBirth':forms.DateInput(attrs={'type':'date',}),
            'name':forms.TextInput(attrs={'placeholder':'name..','id':'campo_actual','data-error':'write the name'}),
            'lastName':forms.TextInput(attrs={'placeholder':'last name..','id':'campo_actual'}),
            'email':forms.EmailInput(attrs={'placeholder':'example@example.com'}),
            'marital':forms.RadioSelect(choices=MARITAL, attrs={'class':'form-check-radio'}),
            'authorize': forms.CheckboxInput(attrs={'type':'checkbox', 'id':'fexamplecheck1', 'class':'form-check-input','name':'fexamplecheck1'}),
            'agree': forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'agreeTerms': forms.CheckboxInput(attrs={'class':'form-check-input'}),
            # 'imagen':forms.FileInput(attrs={'class':'form-control'})
        }
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            
            # self.fields['imagen'].widget.attrs.update(
            #     {'accept': '.jpg, .jpeg, .png, .gif'}) 