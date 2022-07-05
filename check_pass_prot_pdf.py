from PyPDF2 import PdfFileReader, PdfFileWriter
document = PdfFileReader("axis_no_ifsc_ CARE886121926.pdf")

if document.isEncrypted:
    print("protected")
else:
    print("not protected")
