from django.db import models

# Create your models here.

class MyReport(models.Model):
    name = models.CharField('Report', max_length=30)

class MyReportNew(models.Model):
    name = models.CharField('ReportNew', max_length=30)
    email = models.EmailField('EmailNew', blank=True)

class SeriousBank(models.Model):
    charDocument = models.CharField('DocumentNr', max_length=15)
    dateExecute = models.DateField('ExecuteDate', auto_now=False)

    charPayer = models.CharField('PayerName', max_length=50)
    charPayerReg = models.CharField('PayerRegNr', max_length=20)
    charPayerAccount = models.CharField('PayerAccountNr', max_length=25)
    charPayerBank = models.CharField('PayerBankSWIFT', max_length=10)

    charReceiver = models.CharField('ReceiverName', max_length=50)
    charReceiverAccount = models.CharField('ReceiverAccountNr', max_length=25)
    charReceiverBank = models.CharField('ReceiverBankSWIFT', max_length=10)
    charReceiverReg = models.CharField('ReceiverRegNr', max_length=20)

    floatSum = models.FloatField('Sum')
    charAim = models.CharField('PaymentAim', max_length=250)
    floatCost = models.FloatField('ServiceCost')

