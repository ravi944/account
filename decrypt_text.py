# importing required modules
import PyPDF2


# creating a pdf file object
pdfFileObj = open('axis_no_ifsc_ CARE886121926.pdf', 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
password = "CARE886121926"
if pdfReader.isEncrypted:
    pdfReader.decrypt(password)

# printing number of pages in pdf file
print(pdfReader.numPages)

# creating a page object
pageObj = pdfReader.getPage(0)

# extracting text from page
text=pageObj.extractText()
print(text)

# closing the pdf file object
pdfFileObj.close()
