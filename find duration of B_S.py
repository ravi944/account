import PyPDF2
import pandas as pd
from datetime import datetime, date
# creating a pdf file object
pdfFileObj = open('union_1.pdf', 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# printing number of pages in pdf file
print(pdfReader.numPages)

# creating a page object
pageObj = pdfReader.getPage(0)

# extracting text from page
text=pageObj.extractText()
import re
# print(page_data)
pattern1 = re.findall(r"[0-9]{2}/[0-9]{2}/[0-9]{1,2}", text)
start_date=str(pattern1[0])

end_date=str(pattern1[1])
# convert string to date object
d1 = datetime.strptime(start_date, "%d/%m/%y")
d2 = datetime.strptime(end_date, "%d/%m/%y")

# difference between dates in timedelta
delta = d2 - d1
print(f'Difference is {delta.days} days')
if delta.days<=160:
    print("bank statement accepted")
else:
    print("bank statement not accepted")
pdfFileObj.close()
