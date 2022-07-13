
import PyPDF2
import re
import dateutil.parser as dparser
from datetime import datetime, date
pdfFileObj = open('PNB_d.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReader.numPages)
pageObj = pdfReader.getPage(0)
text=pageObj.extractText()
pattern1 = re.findall(r"[0-9]{2}/[0-9]{2}/[0-9]{1,4}|[0-9]{2}-[0-9]{2}-[0-9]{1,4}|[0-9]{2}/[a-zA-Z]{3}/[0-9]{1,4}|[0-9]{2}-[a-zA-Z]{3}-[0-9]{1,4}", text)
start_date=pattern1[0]
end_date=pattern1[1]
x=dparser.parse(start_date,fuzzy=True).date()
y=dparser.parse(end_date,fuzzy=True).date()
a=str(x)
b=str(y)
print(a)
print(b)
d1 = datetime.strptime(a, "%Y-%m-%d")
d2 = datetime.strptime(b, "%Y-%m-%d")
delta = d2 - d1
print(f'Difference is {delta.days} days')
if delta.days<=160:
    print("bank statement accepted")
else:
    print("not accepted")
pdfFileObj.close()
