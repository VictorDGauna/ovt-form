from django.db import models
from datetime import datetime

# Create your models here.
class Bildens_model(models.Model):
    who = models.TextField('who',max_length=100, blank=True, null=True)
    CREDIT_ENRICHMENT='Credit Enrichment'
    INSURANCE='Insurance'
    TAXES='Taxes'
    ACCOUNTING='Accounting'
    PAYROLL='Payroll'
    BOOKEEPING='Bookeeping'
    MARKETING='Marketing'
    LOANS='Loans'
     
    serviceOption_choices = [
        (CREDIT_ENRICHMENT,"Credit Enrichment"),
        (INSURANCE,"Insurance"),
        (TAXES,"Taxes"),
        (ACCOUNTING,"Accounting"),
        (PAYROLL,"Payroll"),
        (BOOKEEPING,"Bookkeeping"),
        (MARKETING,"Marketing"),
        (LOANS ,"Loans"),
    ]
    
    serviceOption = models.CharField('',max_length=100,choices=serviceOption_choices,blank=True, null=True)
    creditEnrichment = models.TextField('',max_length=255,blank=True, null=True)
    scores = models.TextField('',blank=True, null=True)
    name = models.CharField('name',max_length=100 )
    lastName = models.CharField('',max_length=100,default='')
    
    dateOfBirth = models.DateField('',auto_now=False,blank=True, null=True)
    numberSecurity = models.CharField('',max_length=100, default='')
    driversLicense = models.CharField('',max_length=100,default='')
    marital = models.CharField('',max_length=10)
    email = models.EmailField('',max_length=100,default='')
    codeArea = models.CharField('Code Area',max_length=100,default='')
    phoneNumber = models.CharField('Phone Number',max_length=100,default='')
    codeCellArea= models.CharField('Code Area',max_length=100,default='' )
    cellNumber= models.CharField('Cell Number',max_length=100,default='' )
    streetAdress= models.CharField('Street Adress',max_length=100,default='' )
    aptAdress= models.CharField('Apt/Adress',max_length=100, default='' )
    city=models.CharField('City',max_length=100, default='' )
    state=models.CharField('State',max_length=100, default='' )
    zipCode=models.CharField('Zip Code',max_length=100,default='' )
    moved = models.TextField('',blank=True, null=True)
    previousAdress= models.TextField('',blank=True, null=True)
    employer= models.TextField('',default='')
    hireDate= models.TextField('',blank=True, null=True) 
    employeeId= models.TextField('',blank=True, null=True)
    work= models.TextField('',default='')
    gross= models.CharField('',max_length=100,default='')
    rent=models.CharField('',max_length=100, default='')
    insurance=models.CharField('',max_length=100, blank=True, null=True)
    loan=models.TextField('',blank=True, null=True)
    authorize= models.BooleanField('Yes',null=True)
    agree=models.BooleanField('Yes',null=True)
    agreeTerms=models.BooleanField('', null=True)
    imagen=models.ImageField(upload_to='images', null=True)
    
    
    class Meta:
        verbose_name ='Bildens_Model'
        verbose_name_plural ='Bildens_Model'
    
    
    def __str__(self):
        return str(self.name)