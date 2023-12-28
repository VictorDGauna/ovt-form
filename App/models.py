from django.db import models
from datetime import datetime

# Create your models here.
class Bildens_model(models.Model):
    who = models.TextField('Who Reffered',max_length=100, blank=True, null=True)
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
    
    serviceOption = models.CharField('Services',max_length=100,choices=serviceOption_choices,blank=True, null=True)
    creditEnrichment = models.TextField('Credit Enrichment',max_length=255,blank=True, null=True)
    scores = models.TextField('Scores',blank=True, null=True)
    name = models.CharField('Name',max_length=100 )
    lastName = models.CharField('Last Name',max_length=100,default='')
    
    dateOfBirth = models.DateField('Date oF Bitrh',auto_now=False,blank=True, null=True)
    numberSecurity = models.CharField('Security Number',max_length=100, default='')
    driversLicense = models.CharField('Drivers License',max_length=100,default='')
    marital = models.CharField('Marital Status',max_length=10)
    email = models.EmailField('Email',max_length=100,default='')
    codeArea = models.CharField('Code Area',max_length=100,default='')
    phoneNumber = models.CharField('Phone Number',max_length=100,default='')
    codeCellArea= models.CharField('Code Area',max_length=100,default='' )
    cellNumber= models.CharField('Cell Number',max_length=100,default='' )
    streetAdress= models.CharField('Street Adress',max_length=100,default='' )
    aptAdress= models.CharField('Apt/Adress',max_length=100, default='' )
    city=models.CharField('City',max_length=100, default='' )
    state=models.CharField('State',max_length=100, default='' )
    zipCode=models.CharField('Zip Code',max_length=100,default='' )
    moved = models.TextField('Moved',blank=True, null=True)
    previousAdress= models.TextField('Previous Adress',blank=True, null=True)
    employer= models.TextField('Employer',default='')
    hireDate= models.TextField('Hire Date',blank=True, null=True) 
    employeeId= models.TextField('Employee ID',blank=True, null=True)
    work= models.TextField('Work',default='')
    gross= models.CharField('Gross',max_length=100,default='')
    rent=models.CharField('Rent',max_length=100, default='')
    insurance=models.CharField('Insurance',max_length=100, blank=True, null=True)
    loan=models.TextField('Loan',blank=True, null=True)
    authorize= models.BooleanField('Authorize',null=True)
    agree=models.BooleanField('Agree',null=True)
    agreeTerms=models.BooleanField('Agree Terms', null=True)
    imagen=models.ImageField('Sign',upload_to='images', null=True)
    
    
    class Meta:
        verbose_name ='Bildens_Model'
        verbose_name_plural ='Bildens_Model'
    
    
    def __str__(self):
        return str(self.name)