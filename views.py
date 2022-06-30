import re
import PyPDF2
from django.http import HttpResponse

from django.shortcuts import render

#Create your views here.

def get_details(request):
    import PyPDF2
    pdfFileObj = open('Bank Statement.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)


    print(pdfReader.numPages)
    pageObj = pdfReader.getPage(0)
    text = pageObj.extractText()
    print(text)
    pdfFileObj.close()
    return HttpResponse(text)

def first_date(request):
    import re
    pdfFileObj = open('Bank Statement.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    print(pdfReader.numPages)
    pageObj = pdfReader.getPage(0)
    text = pageObj.extractText()
    pdfFileObj.close()
    pattern = re.findall(r"[a-zA-Z]{3} [0-9]{1,2}", text)
    print("first date", pattern[0])
    return HttpResponse(pattern[0])
def last_date(request):
    import re
    pdfFileObj = open('Bank Statement.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    print(pdfReader.numPages)
    pageObj = pdfReader.getPage(0)
    text = pageObj.extractText()
    pdfFileObj.close()
    pattern = re.findall(r"[a-zA-Z]{3} [0-9]{1,2}", text)
    print("last date", pattern[-1])
    return HttpResponse(pattern[-1])


def acc_num(request):
    import re
    pdfFileObj = open('Bank Statement.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    print(pdfReader.numPages)
    pageObj = pdfReader.getPage(0)

    text = pageObj.extractText()
    pdfFileObj.close()
    acc_pattern = re.findall(r"\d{2}-\d{6}", text)
    for s in acc_pattern:
        print("Account number is :-", s)
    return HttpResponse(acc_pattern)




def ifsc_code(request):
    pdfFileObj = open('Bank Statement.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    print(pdfReader.numPages)

    pageObj = pdfReader.getPage(0)

    text = pageObj.extractText()
    pdfFileObj.close()
    ifsc_pattern = re.findall(r"0\d{5}", text)
    for i in ifsc_pattern:
        print("ifsc code is:-",i)
    return HttpResponse(ifsc_pattern)

